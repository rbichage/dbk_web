from rest_framework import viewsets, generics
from rest_framework.views import APIView

from accounts.models import News
from api_dbk.news.serializers import NewsSerializer


class NewsViewSet(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

