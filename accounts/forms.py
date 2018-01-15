from django.contrib.auth.forms import UserCreationForm

from accounts.models import Donor


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Donor
        fields = {'username', 'first_name', 'last_name', 'gender', 'age',  'blood_group', 'county_name'}