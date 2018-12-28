from datetime import date, timezone

from django.contrib import auth
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models

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

    blood_group = models.CharField(choices=BLOOD_CHOICES, max_length=40, default='choose', null=True, blank=True,)
    date_donated = models.DateField(null=True, blank=True)
    county_name = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(null=True, blank=True, max_length=20,)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to='static/profiles', blank=True)

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
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message=
                                 "Phone number must be entered in the format: '+254712345678'. Up to 15 digits "
                                 "allowed. "
                                 )
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True)
    county_name = models.ForeignKey(County, on_delete=models.CASCADE, null=True)
    schedule_date = models.DateTimeField(auto_now=False, null=True)

    def __str__(self):
        return self.first_name
