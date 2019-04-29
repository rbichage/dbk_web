from rest_framework import serializers

from accounts.models import News


class NewsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    description = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    class Meta:
        model = News
        fields = ('title', 'description', 'created_at', 'image_url')
        read_only_fields = ('created_at', )

    def create(self, validated_data):
        news = News(
            title=self.validated_data['title'],
            description=self.validated_data['description'],
            image_url=validated_data['image_url'],

        )
        news.save()
        return news

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data('description', instance.description)
        instance.image_url = validated_data.get('image_url', instance.image_url)

        instance.save()
        return instance
