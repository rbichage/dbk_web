from datetime import date, timezone

from django.contrib import auth
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models
from django.utils import timezone as tz

# Create your models here.
from django.utils.datetime_safe import datetime


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class News(models.Model):
    title = models.CharField(max_length=100, help_text='max. of One hundred characters')
    description = models.TextField(null=True)
    # image_url = models.ImageField(
    #     upload_to=upload_location,
    #     null=True, blank=True,
    #     width_field="width_field",
    #     height_field="height_field")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title

    def body(self):
        return self.description

    body.allow_tags = True


class County(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Counties"


class Donor(auth.models.User):
    Male = 1
    Female = 2
    NOT_SET = 0
    A_pos = 3
    # A_neg =
    # B_pos =
    # B_neg =
    #
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),

    )
    BLOOD_CHOICES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),

    )
    birthdate = models.DateField(null=True)

    @property
    def age(self):
        if self.birthdate is None:
            return None
        return int((datetime.now().date() - self.birthdate).days / 365.25)

    blood_group = models.CharField(choices=BLOOD_CHOICES, max_length=40, default='choose', null=True, blank=True, )
    date_donated = models.DateField(null=True, blank=True, auto_now=False)
    county_name = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(null=True, blank=True, max_length=20, )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to='static/profiles', blank=True)
    has_appointment = models.SmallIntegerField(null=True, blank=True)
    schedule_date = models.DateField(auto_now=False, blank=True, null=True)
    has_donated = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Donors"


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=100)
    county_name = models.ForeignKey(County, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.hospital_name


class Event(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=500)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Events'


class Appointment(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message=
                                 "Phone number must be entered in the format: '+254712345678'. Up to 15 digits "
                                 "allowed. "
                                 )
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True)
    county_name = models.ForeignKey(County, on_delete=models.CASCADE, null=True)
    hospital_name = models.CharField(max_length=140, null=True, blank=True)
    schedule_date = models.DateField(auto_now=False, null=True)
    has_donated = models.BooleanField(null=True, blank=True)
    date_donated = models.DateField(null=True, auto_now=False)
    amount_donated = models.SmallIntegerField(null=True, blank=True, help_text="mls")

    def __str__(self):
        return self.username

    @property
    def has_appointment(self):
        return self.schedule_date > tz.now()

    def save(self, **kwargs):
        donor = Donor.objects.get(self.username)
        donor.date_donated = self.date_donated
        donor.has_appointment = self.has_appointment
        donor.schedule_date = self.schedule_date
        donor.has_donated = self.has_donated

        return super(Appointment, self).save(**kwargs)
