from django.conf.urls import url
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login


from accounts import views
# from api_dbk.viewsets import DonorViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^register/$', views.register, 'register'),

    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^admin/helper/detail/(?P<pk>\d+)$', login_required(views.DonorDetailView.as_view()), name='helper_detail'),

    url(r'^help/login/$', login, name='dbk-login'),
    url(r'^logout-then-login/$', logout_then_login, name='logout-then-login'),

]


