

from django.conf.urls import url
from django.contrib.auth.views import login

from accounts import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/', login, {'template_name': 'accounts/login.html'}),
    url(r'^logout/', login, {'template_name': 'accounts/logout.html'}),

]
