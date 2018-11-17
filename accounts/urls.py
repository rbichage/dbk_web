from django.conf.urls import url
from accounts import views
# from api_dbk.viewsets import DonorViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^register/$', views.register, 'register'),

]


