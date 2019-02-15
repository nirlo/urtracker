from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'urtracker'

urlpatterns = [
    url(r'^$', views.main, name="main"),
    url(r'^track/$', views.track, name="track"), 
    url(r'^get_tracker_info/$', views.get_tracker_info, name="get_tracker_info")
]