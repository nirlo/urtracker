from django import forms
from . import models

class TrackInfo(forms.ModelForm):
    class Meta:
        model = models.Tracker
        fields = [
            'title',
            'over_all_feeling',
            'workout',
            'workout_type',
            'headspace',
            'sad_lamp',
            'vitd',
            'omega3',
            'conflict',
            'accomplish',
            'sleep',
            'eating',
            'rating',
        ]