from abc import ABC

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_jwt.settings import api_settings

from accounts.models import Donor
from api_dbk.counties.serializers import CountySerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField()


class DonorProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=False, required=False, allow_null=True, allow_blank=True)
    first_name = serializers.CharField(read_only=False, required=False, allow_null=True, allow_blank=True)
    last_name = serializers.CharField(read_only=False, required=False, allow_null=True, allow_blank=True)
    phone_number = serializers.CharField(read_only=False, required=False, allow_null=True, validators=[
        UniqueValidator(
            queryset=Donor.objects.all(),
            message="Phone number already in use",
        )])
    birthdate = serializers.DateField(read_only=False, required=False, allow_null=True)
    gender = serializers.IntegerField(required=False, read_only=False, allow_null=True)

    class Meta:
        model = Donor
        fields = (
            'id', 'username', 'first_name', 'last_name', 'username', 'gender', 'phone_number', 'birthdate',
            'email',
            'image_url',
            'image_url'
        )

        read_only_fields = ('updated_at', 'created_at')

    def update(self, instance, validated_data):
        print("gender is " + str(validated_data['gender']))

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.save()

        return instance


class SignUpSerializer(serializers.ModelSerializer):
    # county = CountySerializer(required=False)
    # county_name = serializers.CharField(max_length=50, required= False, allow_null=True)
    email = serializers.EmailField(required=True, allow_null=False)

    username = serializers.CharField(max_length=50, required=True, allow_null=False, validators=[
        UniqueValidator(queryset=Donor.objects.all(), message="username  already in use", )])
    first_name = serializers.CharField(max_length=50, required=True, allow_null=False)
    last_name = serializers.CharField(max_length=50, required=True, allow_null=False)

    class Meta:
        model = Donor
        fields = ('id', 'username', 'first_name', 'last_name',
                  'password', 'email', 'birthdate', 'gender',

                  'first_name', 'last_name', 'gender')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('updated_at', 'created_at')

    def create(self, validated_data):
        user = Donor(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.set_password(validated_data.get('password'))

        instance.save()
        return instance


class DonorSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = Donor
        fields = ('id', 'username', 'email', 'first_name', 'token',
                  'last_name')
        read_only_fields = ('id', 'token')

    @staticmethod
    def get_token(obj):
        return None


class DonorLoginSerializer(DonorSerializer):
    def get_token(self, obj):
        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

