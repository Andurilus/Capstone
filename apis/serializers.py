from rest_framework import serializers
from photos import models


class ApodPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ApodPhoto
        fields = ('id', 'date', 'url', 'title', 'expanation', 'media')