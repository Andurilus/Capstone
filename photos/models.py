from django.db import models

class ApodPhoto(models.Model):
    title = models.CharField(max_length=200)
    media = models.CharField(max_length=200)
    date = models.DateField()
    url = models.URLField()
    explanation = models.TextField()
    author = models.ForeignKey('users.CustomUser', related_name="posts", on_delete=models.CASCADE)

    def __str__(self):
        return self.title