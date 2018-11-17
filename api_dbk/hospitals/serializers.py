from rest_framework import serializers

from accounts.models import Hospital


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = (
            'id',
            'hospital_name',
            'county_name',
            'phone_number',
        )
