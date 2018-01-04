from django.contrib import admin

# Register your models here.
from accounts.models import Donor, Hospital, County

admin.site.register(Donor),
admin.site.register(Hospital),
admin.site.register(County),


