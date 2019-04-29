from django.contrib import admin

# Register your models here.
from accounts.models import Donor, Hospital, County, Event, News, Appointment, Donation


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


class CountyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')
    # search_fields = ('name',)


# class DonorAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'password',
#         'last_login',
#         'username',
#         'first_name',
#         'last_name',
#         'email',
#         'is_active',
#         'date_joined',
#         'birthdate',
#         'blood_group',
#         'county_name',
#         'gender',
#         'phone_number',
#         'schedule_date',
#         'has_appointment',
#         'has_donated',
#     )
#     # list_filter = (
#     #     'last_login',
#     #     'is_superuser',
#     #     'is_staff',
#     #     'is_active',
#     #     'date_joined',
#     #     'birthdate',
#     #     'county_name',
#     # )


class HospitalAdmin(admin.ModelAdmin):
    list_display = ('hospital_name', 'county_name', 'phone_number')
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
        'created_at',
        'image_url',
    )


admin.site.register(News, NewsAdmin),


class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'county_name',
        'phone_number',
        'schedule_date',
        'date_donated',
        'has_donated',
        'has_appointment',
        'hospital_name',
        'amount_donated',
    )

    readonly_fields = (
        'username',
        'county_name',
        'schedule_date',
        'hospital_name',
        'county_name',
        'phone_number',
    )

    fields = (
        'donor',
        'first_name',
        'last_name',
        'county_name',
        'phone_number',
        'schedule_date',
        'date_donated',
        'has_donated',
        'hospital_name',
        'amount_donated',
    )

    list_filter = (
        'hospital_name',
        'county_name',
        'date_donated',
    )


admin.site.register(Appointment, AppointmentAdmin)


class DonationAdmin(admin.ModelAdmin):
    list_display = (
        'donor',
        'date_donated',
        'has_donated',
        'hospital_name',
        'county_name',
        'amount_donated'

    )
    fields = (
        'donor',
        'date_donated',
        'has_donated',
        'hospital_name',
        'county_name',
        'amount_donated',
    )

    list_filter = (
        'donor',
        'county_name',
        'hospital_name',
    )

    search_fields = (
        'donor',
        'hospital_name',
        'county_name',
    )


admin.site.register(Donation, DonationAdmin)


class DonationsTabular(admin.TabularInline):
    model = Donation
    readonly_fields = ('donor',
                       'date_donated',
                       'has_donated',
                       )
    fields = ('donor',
              'date_donated',
              'has_donated',)
    extra = 0


class AppointmentTabular(admin.TabularInline):
    model = Appointment
    readonly_fields = ('schedule_date', 'hospital_name', 'county_name', 'amount_donated', 'times_donated')

    fields = ('schedule_date', 'hospital_name', 'county_name', 'amount_donated', 'times_donated')
    extra = 0


class DonorAdmin(admin.ModelAdmin):
    inlines = (AppointmentTabular, DonationsTabular,)
    list_display = (
        'username',
        'first_name',
        'last_name',
        'birthdate',
        'age',
        'county_name',
        'gender'

    )

    fields = (
        'username',
        'first_name',
        'last_name',
        'birthdate',
        'county_name',
        'gender'

    )


admin.site.register(Donor, DonorAdmin),
