from django.contrib import auth
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.


class County(models.Model):
    name = models.CharField(max_length=20)

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
    email = models.EmailField
    age = models.IntegerField(default=18, validators=[MinValueValidator(18),
                                                      MaxValueValidator(55)])

    blood_group = models.CharField(choices=BLOOD_CHOICES, max_length=4, default='choose')
    county_name = models.ForeignKey(County, on_delete=models.CASCADE)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=NOT_SET)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = "Donors"


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=100)
    county_name = models.ForeignKey(County, on_delete=models.CASCADE)

    def __str__(self):
        return self.hospital_name
