from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Tracker(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='trackdata')
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    over_all_feeling = models.CharField(max_length=200)
    workout = models.BooleanField()
    workout_type = models.CharField(max_length=200)
    headspace = models.BooleanField() 
    sad_lamp = models.BooleanField()
    vitd = models.BooleanField()
    omega3 = models.BooleanField()
    conflict = models.BooleanField()
    accomplish = models.BooleanField()
    sleep = models.IntegerField()
    eating = models.TextField()
    rating = models.IntegerField(
        default = 1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )

    def __str__(self):
        return self.title