from django.db import models
from django.contrib.auth import get_user_model

class ApodPhoto(models.Model):
    title = models.CharField(max_length=200)
    media = models.CharField(max_length=200)
    date = models.DateField()
    url = models.URLField()
    explanation = models.TextField()
    author = models.ForeignKey(get_user_model(), related_name="apodposts", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class MarsPhoto(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    sol = models.CharField(max_length=200)
    earth_date = models.CharField(max_length=200)
    date = models.DateField()
    rover = models.CharField(max_length=200)
    camera_name = models.CharField(max_length=200)
    url = models.URLField()
    explanation = models.TextField(null=True, blank=True)
    author = models.ForeignKey(get_user_model(), related_name="marsposts", on_delete=models.CASCADE)

    def __str__(self):
        return self.title