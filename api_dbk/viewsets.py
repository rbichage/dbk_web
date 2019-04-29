from rest_framework import viewsets, filters
from rest_framework.filters import SearchFilter

from accounts.models import Donor, County, Hospital, Event, Donation, Appointment
from api_dbk.appointments.serializers import AppointmentSerializer
from api_dbk.counties.serializers import CountySerializer
from api_dbk.donations.serializers import DonationSerializer
from api_dbk.donors.donor_serializers import DonorSerializer, DonorProfileSerializer
from api_dbk.events.serializers import EventSerializer
from api_dbk.hospitals.serializers import HospitalSerializer


class DonorViewSet(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer


class CountyViewSet(viewsets.ModelViewSet):
    queryset = County.objects.all()
    serializer_class = CountySerializer


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('county_name',)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    filter_backends = (filters.SearchFilter,)
    filter_fields = ('donor',)


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = (filters.SearchFilter,)
    filter_fields = ('donor',)


