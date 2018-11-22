from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import County, News


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id', 'email', 'username', 'first_name', 'last_name')


class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = ('id', 'code', 'name')

    def create(self, validated_data):
        country = County(
            name=validated_data['name'],
        )
        country.save()
        return country

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)

        instance.save()
        return instance


class NewsSerializer(serializers.ModelSerializer):
    admin = AdminSerializer(required=False)

    class Meta:
        model = News
        fields = ('id', 'title', 'description', 'image_url',
                  'video_url', 'admin', 'updated_at', 'created_at', 'admin_id')
        read_only_fields = ('updated_at', 'created_at')

    def create(self, validated_data):
        news = News(
            title=validated_data['title'],
            description=validated_data['description'],
            image_url=validated_data['image_url'],
            admin=validated_data['admin']
        )
        news.save()
        return news

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.video_url = validated_data.get('video_url', instance.video_url)
        instance.admin = validated_data.get('admin', instance.admin)

        instance.save()
        return instance
