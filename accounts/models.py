from django.contrib import auth
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models


# Create your models here.


class County(models.Model):
    CODE_CHOICES = [(i, str(i)) for i in range(1, 46)]

    name = models.CharField(max_length=20, unique=True)
    code = models.IntegerField(default='1', unique=True)

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
        (Male, 'male'),
        (Female, 'female'),
        (NOT_SET, 'Not Set'),
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
    age = models.IntegerField(default=18, validators=[MinValueValidator(18),
                                                      MaxValueValidator(55)])

    blood_group = models.CharField(choices=BLOOD_CHOICES, max_length=4, default='choose')
    county_name = models.ForeignKey(County, on_delete=models.CASCADE)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=NOT_SET)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message=
                                 "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
                                 )
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = "Donors"


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=100)
    county_name = models.ForeignKey(County, on_delete=models.CASCADE)

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
