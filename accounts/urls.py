from django.conf.urls import url

from accounts import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^list', views.donor_list, name='list'),
]
