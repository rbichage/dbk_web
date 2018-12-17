from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_dbk import views as api_view
from api_dbk.donors import views
from api_dbk.viewsets import CountyViewSet

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    # login : provide username and password : @return user,token
    path(r'login/', views.login),
    path(r'signup/', views.SignUpView.as_view()),
    path(r'appointments/', api_view.AppointmentList.as_view()),

    # Update user profile

    url(r'^donors/profile/$', api_view.DonorProfileList.as_view()),

    url(r'^donors/profile/(?P<pk>[0-9]+)/$', api_view.DonorProfileDetails.as_view()),
    url(r'^appointments/(?P<pk>[0-9]+)$', api_view.AppointmentDetails.as_view()),
    # path(r'profile/(?P<pk>[0-9]+)/', api_view.DonorProfileDetails.as_view()),

]

# login_router = DefaultRouter()
# login_router.register('login', views.login)
# urlpatterns += login_router.urls
#
county_router = DefaultRouter()
county_router.register('counties', CountyViewSet)

urlpatterns += county_router.urls
#
# news_router = DefaultRouter()
# news_router.register('news', AppointmentList)
# urlpatterns += news_router.urls
#
# hospital_router = DefaultRouter()
# hospital_router.register('hospitals', HospitalViewSet)
# urlpatterns += hospital_router.urls
#
# event_router = DefaultRouter()
# event_router.register('events', EventViewSet)
# urlpatterns += event_router.urls
