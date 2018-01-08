from django.core import serializers
from django.db.models.sql import Query
from django.http import HttpResponse
from django.shortcuts import render
from accounts.models import Donor, Hospital, County


# Create your views here.

def home(request):
    return render(request, 'accounts/index.html')


def donor_list(request):
    data = serializers.serialize('json', Donor.objects.all())
    data = serializers.serialize('json', data)
    return HttpResponse(data, content_type='application/json')
