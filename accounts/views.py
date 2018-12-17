from django.contrib.auth import authenticate
from django.core import serializers
from django.db.models.sql import Query
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from accounts.models import Donor, Hospital, County
from accounts.forms import UserCreationForm, LoginForm


# Create your views here.

def home(request):
    return render(request, 'dbk/layouts/index.html')


def user_login(request):
    if request.user.is_authenticated:
        return render(request, 'dbk/accounts/dashboard.html', {})
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponse('Authenticated successfully')
                    else:
                        return HttpResponse('Disabled Account')
                else:
                    return HttpResponse('Invalid login')
        else:
            form = LoginForm()
        return render(request, 'dbk/accounts/login.html', {'form': form})


def dashboard(request):
    return None


class DonorDetailView(generic.DetailView):
    model = Donor

    def get_context_data(self, **kwargs):
        ctx = super(DonorDetailView, self).get_context_data(**kwargs)
        return ctx
