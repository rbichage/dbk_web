from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import County, News, Hospital


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id', 'email', 'username', 'first_name', 'last_name')


class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = ('id', 'name')

    def create(self, validated_data):
        county = County(
            name=validated_data['name'],
        )
        county.save()
        return county

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)

        instance.save()
        return instance


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'description',
                  'updated_at', 'created_at')

        read_only_fields = ('updated_at', 'created_at')

    def create(self, validated_data):
        news = News(
            title=validated_data['title'],
            description=validated_data['description'],
        )
        news.save()
        return news

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class CountyHospitalSerializer(serializers.ModelSerializer):
    county_name = serializers.CharField(max_length=40)

    class Meta:
        model = Hospital,
        fields = ('county_name', 'hospital_name',
                  'county_name', 'hospital_name')


class HospitalSerializer(serializers.ModelSerializer):
    fields = (
        'id', 'hospital_name', 'county_name'
    )
