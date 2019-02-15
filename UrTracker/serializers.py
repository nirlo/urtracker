from django.core import serializers
from .models import Tracker

class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackerSerializer
        fields = ['rating', 'date']