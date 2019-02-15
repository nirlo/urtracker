from django.shortcuts import render, redirect
from django.core import serializers
from django.forms.models import model_to_dict
from .models import Tracker
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import forms
import requests
# Create your views here.

@login_required(login_url="/accounts/login/")
def main(request):
    return render(request, 'UrTracker/main.html')

@login_required(login_url="/accounts/login/")
def track(request):
    if request.method == 'POST':
        form = forms.TrackInfo(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.User = request.user
            instance.save()
            return redirect('urtracker:main')
    else:
        form = forms.TrackInfo()
    return render(request, 'UrTracker/track.html', {'form': form})

def get_tracker_info(request):
    data = Tracker.objects.all()
    data_json = serializers.serialize('json', data)
    return HttpResponse(data_json, content_type='application/json')
