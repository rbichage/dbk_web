from rest_framework import viewsets, permissions
from accounts.models import Donor, County, Hospital, Event, Appointment
from api_dbk.appointments.serializers import AppointmentSerializer
from api_dbk.counties.serializers import CountySerializer
from api_dbk.events.serializers import EventSerializer
from api_dbk.hospitals.serializers import HospitalSerializer


# class DonorViewSet(viewsets.ModelViewSet):
#     queryset = Donor.objects.all()
#     serializer_class = DonorSerializer
#     http_method_names = ['post', 'head', 'get']


class CountyViewSet(viewsets.ModelViewSet):
    queryset = County.objects.all()
    serializer_class = CountySerializer


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer



