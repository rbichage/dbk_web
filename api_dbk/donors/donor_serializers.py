from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_jwt.settings import api_settings

from accounts.models import Donor

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class DonorProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=False, required=False, allow_null=True, allow_blank=True)
    first_name = serializers.CharField(read_only=False, required=False, allow_null=True, allow_blank=True)
    last_name = serializers.CharField(read_only=False, required=False, allow_null=True, allow_blank=True)
    email = serializers.EmailField(read_only=False, required=False, allow_null=True, allow_blank=True)
    gender = serializers.CharField(required=False, read_only=False, allow_null=True)
    county_name = serializers.CharField(read_only=False, required=False, allow_null=True, allow_blank=True)
    blood_group = serializers.CharField(read_only=False, required=False, allow_null=True, allow_blank=True)
    phone_number = serializers.CharField(read_only=False, required=False, allow_null=True)
    birthdate = serializers.DateField(read_only=False, required=False, allow_null=True)
    image = serializers.ImageField(allow_null=True, required=False)

    class Meta:
        model = Donor
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email', 'gender', 'county_name', 'age', 'blood_group', 'phone_number',
            'birthdate', 'image')

        read_only_fields = ('updated_at', 'created_at')

    def update(self, instance, validated_data):

        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.county_name = validated_data.get('county_name', instance.county_name)
        instance.blood_group = validated_data.get('blood_group', instance.blood_group)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.image = validated_data.get('image', instance.image)
        instance.save()

        return instance


class SignUpSerializer(serializers.ModelSerializer):
    # county = CountySerializer(required=False)
    # county_name = serializers.CharField(max_length=50, required= False, allow_null=True)
    email = serializers.EmailField(required=True, allow_null=False, validators=[
        UniqueValidator(queryset=Donor.objects.all(), message="email  already in use", )])

    username = serializers.CharField(max_length=50, required=True, allow_null=False, validators=[
        UniqueValidator(queryset=Donor.objects.all(), message="username  already in use", )])
    first_name = serializers.CharField(max_length=50, required=True, allow_null=False)
    last_name = serializers.CharField(max_length=50, required=True, allow_null=False)
    birthdate = serializers.CharField(max_length=20, required=False, allow_null=True)
    county_name = serializers.CharField(max_length=40, required=False, allow_null=True)
    gender = serializers.CharField(max_length=20, required=False, allow_null=True)

    class Meta:
        model = Donor
        fields = ('id', 'username', 'email', 'first_name', 'token', 'gender',
                  'last_name', 'birthdate', 'county_name', 'age', 'phone_number', 'blood_group', 'date_donated',
                  'image')
        # fields = ('id', 'username', 'first_name', 'last_name',
        #           'password', 'email', 'birthdate', 'gender', 'county_name',

        #           'first_name', 'last_name', 'gender', 'birthdate', 'county_name')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('updated_at', 'created_at')

    def create(self, validated_data):
        user = Donor(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            birthdate=validated_data['birthdate'],
            county_name=validated_data['county_name'],
            gender=validated_data['gender'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.county_name = validated_data.get('county_name', instance.county_name)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.set_password = (validated_data.get('password'))

        instance.save()
        return instance


class DonorSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = Donor
        fields = ('id', 'username', 'email', 'first_name', 'token', 'gender',
                  'last_name', 'birthdate', 'county_name', 'age', 'phone_number', 'blood_group', 'date_donated',
                  'image')
        read_only_fields = ('id', 'token')

    @staticmethod
    def get_token(obj):
        return None


class DonorLoginSerializer(DonorSerializer):
    def get_token(self, obj):
        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token


class PasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = Donor

    @staticmethod
    def validate_new_password(value):
        validate_password(value)
        return value
