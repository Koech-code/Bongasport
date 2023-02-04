from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Athlete_Post(models.Model):

    # user = models.ForeignKey(User, on_delete=models.CASCADE,  null=True) # many users can many tweets

    video = models.FileField(upload_to='videos/', blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    content = models.TextField(blank=True, null=True)
