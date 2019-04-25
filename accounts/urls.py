from django.conf.urls import url
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login
from django.urls import include

from accounts import views
# from api_dbk.viewsets import DonorViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # url(r'^register/$', views.register, 'register'),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^logout-then-login/$', logout_then_login, name='logout-then-login'),

]


