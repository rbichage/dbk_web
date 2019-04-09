from rest_framework import serializers
from accounts.models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = (
            'id',
            'first_name',
            'last_name',
            'county_name',
            'phone_number',
            'schedule_date',
            'hospital_name',
            'has_appointment'
        )

        @staticmethod
        def create(self, validated_data):
            appointment = Appointment(
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                county_name=validated_data['county_name'],
                phone_number=validated_data['phone_number'],
                hospital_name=validated_data["hospital_name"],
                schedule_date=validated_data['schedule_date']
            )
            appointment.save()
            return appointment

        @staticmethod
        def update(self, instance, validated_data):
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.county_name = validated_data.get('county_name', instance.county_name)
            instance.phone_number = validated_data.get('phone_number', instance.phone_number)
            instance.schedule_date = validated_data.get('schedule_date', instance.schedule_date)
            instance.hospital_name = validated_data.get('hospital_name', instance.hospital_name)

            instance.save()
            return instance
