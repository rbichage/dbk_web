from django.core import serializers
from django.db.models.sql import Query
from django.http import HttpResponse
from django.shortcuts import render
from accounts.models import Donor, Hospital, County
from accounts.forms import UserCreationForm


# Create your views here.

def home(request):
    return render(request, 'accounts/index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)


