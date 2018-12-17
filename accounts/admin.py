from django.contrib import admin

# Register your models here.
from accounts.models import Donor, Hospital, County, Event, News, Appointment


class DonorAdmin(admin.ModelAdmin):
    list_display = ('username',
                    'first_name',
                    'last_name',
                    'birthdate',
                    'age',
                    'date_donated',
                    'county_name',

                    )


admin.site.register(Donor, DonorAdmin),


class HospitalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'hospital_name',
        'county_name',
        'phone_number'
    )


admin.site.register(Hospital, HospitalAdmin),


class CountyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )


admin.site.register(County, CountyAdmin),


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'county',
        'hospital',
        'date'
    )


admin.site.register(Event, EventAdmin)
# vim: set fileencoding=utf-8 :
from django.contrib import admin


class CountyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')
    # search_fields = ('name',)


class DonorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'date_joined',
        'birthdate',
        'blood_group',
        'county_name',
        'gender',
        'phone_number',
    )
    # list_filter = (
    #     'last_login',
    #     'is_superuser',
    #     'is_staff',
    #     'is_active',
    #     'date_joined',
    #     'birthdate',
    #     'county_name',
    # )


class HospitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'hospital_name', 'county_name', 'phone_number')
    # list_filter = ('county_name',)


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'county',
        'hospital',
        'date',
    )
    # list_filter = ('county', 'hospital', 'date')
    # search_fields = ('name',)


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'created_at'
    )


admin.site.register(News, NewsAdmin),


class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'county_name',
        'phone_number',
        'schedule_date',
    )


admin.site.register(Appointment, AppointmentAdmin),
