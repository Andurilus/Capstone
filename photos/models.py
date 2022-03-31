from django.db import models

class ApodPhoto(models.Model):
    title = models.CharField(max_length=200)
    media = models.CharField(max_length=200)
    date = models.DateField()
    url = models.URLField()
    explanation = models.TextField()

    def __str__(self):
        return self.title