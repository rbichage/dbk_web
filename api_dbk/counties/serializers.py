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
    title = serializers.CharField(max_length=100, help_text='max. of One hundred characters')
    description = serializers.CharField(max_length=4000, allow_null=True)
    created_at = serializers.DateField(allow_null=True)
    image_url = serializers.ImageField(allow_null=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'description', 'image_url',
                  'created_at')

        read_only_fields = ('created_at',)

    def create(self, validated_data):
        news = News(
            title=validated_data['title'],
            description=validated_data['description'],
            image_url=validated_data['image_url'],
        )
        news.save()
        return news

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image_url = validated_data.get('image_url', instance.image_url)
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
