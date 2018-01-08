from django.contrib import admin

# Register your models here.
from accounts.models import Donor, Hospital, County, Event

admin.site.register(Donor),
admin.site.register(Hospital),
admin.site.register(County),
admin.site.register(Event)


