import sys

from django.http import Http404
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Donor, County, News, Appointment, Hospital
from api_dbk.appointments.serializers import AppointmentSerializer
from api_dbk.counties.serializers import CountySerializer, NewsSerializer, HospitalSerializer
from api_dbk.donors.donor_serializers import DonorProfileSerializer


class CountyList(generics.ListCreateAPIView):
    queryset = County.objects.all()
    serializer_class = CountySerializer
    permission_classes = (permissions.IsAuthenticated,)


class NewsList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = News.objects.all()
    serializer_class = NewsSerializer


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


class HospitalList(generics.ListAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class CountyHospitalsList(APIView):

    @staticmethod
    def get(request):
        county_name = Hospital.objects.filter(county_name="Nairobi")
        county_hospitals = HospitalSerializer(data=request.data)
        response = Response({
            "county": county_name,
            "hospitals": county_hospitals.data
        })

        return response


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
                response = Response({
                    "success": True,
                    "message": "Profile updated successfully",
                    "donor": serializer.data
                })
                response.reason_phrase = "updated successfully"
                response.status_code = 200
                return response

            response = Response({"success": False, "message": serializer.errors}, 400)
            response.reason_phrase = serializer.error_messages['phone_number']

            return response
        except Exception as exception:
            response = Response({"success": False, "message": str(exception), "cause": str(sys.exc_info()[2])},
                                406)
            response.reason_phrase = str(exception)
            return response

    def delete(self, request, pk):
        donor = self.get_object(pk)
        donor.delete()
        return Response(request, 204)
