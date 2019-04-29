from rest_framework import serializers

from accounts.models import Donation


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = (
            'donor',
            'username',
            'date_donated',
            'hospital_name',
            'county_name',
            'amount_donated',

        )
