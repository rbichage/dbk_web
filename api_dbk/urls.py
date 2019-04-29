from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_dbk import views as api_view
from api_dbk.donors import views
from api_dbk.viewsets import HospitalViewSet, DonorViewSet, DonationViewSet, AppointmentViewSet

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    # login : provide username and password : @return user,token
    path(r'login/', views.login),
    path(r'update-password/', views.UpdatePassword.as_view()),
    path(r'signup/', views.SignUpView.as_view()),
    # path(r'appointments/', api_view.AppointmentList.as_view()),
    # path(r'hospitals/', api_view.HospitalList.as_view()),
    path(r'countylist/', api_view.CountyList.as_view()),
    path(r'news/', api_view.NewsList.as_view()),
    url('^hospitals-list/(?P<county_name>.+)/$', api_view.CountyHospitalsList.as_view()),

    # Update user profile

    # path(r'^donors/profile/', api_view.DonorProfileList.as_view()),

    # url(r'^donors/profile/(?P<pk>[0-9]+)/$', api_view.DonorProfileDetails.as_view()),

    # path(r'donors/profile/<int:pk>/', api_view.DonorProfileDetails.as_view()),
    # url(r'^appointments/(?P<pk>[0-9]+)$', api_view.AppointmentDetails.as_view()),
    # path(r'profile/(?P<pk>[0-9]+)/', api_view.DonorProfileDetails.as_view()),

    path(r'news/', api_view.NewsList.as_view()),

]

hospital_router = DefaultRouter()
hospital_router.register('hospitals', HospitalViewSet)
urlpatterns += hospital_router.urls


donor_router = DefaultRouter()
donor_router.register('donors/profile', DonorViewSet)
urlpatterns += donor_router.urls

donations_router = DefaultRouter()
donations_router.register('donations', DonationViewSet)
urlpatterns += donations_router.urls

appointment_router = DefaultRouter()
appointment_router.register('appointments', AppointmentViewSet)
urlpatterns += appointment_router.urls
