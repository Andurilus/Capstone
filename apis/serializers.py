from rest_framework import serializers
from photos import models
from django.contrib.auth import get_user_model

class NestedApodPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ApodPhoto
        fields = ('id', 'author', 'date', 'title', 'url', 'explanation', 'media')

class ApodPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ApodPhoto
        fields = ('id', 'author', 'date', 'title', 'url', 'explanation', 'media')

class UserSerializer(serializers.ModelSerializer):
    apodposts = NestedApodPhotoSerializer(read_only=True, many=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'apodposts')