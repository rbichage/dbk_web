import sys

from django.http import Http404
from rest_framework import generics, status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.compat import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView

from accounts.models import Donor, County, News, Appointment
from api_dbk.appointments.serializers import AppointmentSerializer
from api_dbk.counties.serializers import CountySerializer, NewsSerializer
from api_dbk.donors.donor_serializers import DonorProfileSerializer


class CountyList(generics.RetrieveUpdateDestroyAPIView):
    queryset = County.objects.all()
    serializer_class = CountySerializer
    permission_classes = ()


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (permissions.IsAuthenticated,)


class NewsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (permissions.IsAuthenticated,)


class DonorProfileList(generics.ListCreateAPIView):
    queryset = Donor.objects.all()
    serializer_class = DonorProfileSerializer
    permission_classes = ()


class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AppointmentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = (permissions.IsAuthenticated,)


# update user profile


class DonorProfileDetails(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return Donor.objects.get(pk=pk)
        except Donor.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        donor = self.get_object(pk)
        serializer = DonorProfileSerializer(donor)
        return Response(request, serializer.data)

    def put(self, request, pk):
        try:
            donor = self.get_object(pk)
            serializer = DonorProfileSerializer(donor, data=request.data)

            if serializer.is_valid():
                serializer.save()
                response = Response(serializer.data)
                response.reason_phrase = "Profile successfully updated"
                return response
            response = Response({"success": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            response.reason_phrase = serializer.error_messages['phone_number']
            return response
        except Exception as exception:
            response = Response({"success": False, "message": str(exception), "cause": str(sys.exc_info()[2])},
                                status=status.HTTP_406_NOT_ACCEPTABLE)
            response.reason_phrase = str(exception)
            return response

    def delete(self, request, pk):
        donor = self.get_object(pk)
        donor.delete()
        return Response(request, status=status.HTTP_204_NO_CONTENT)
