from rest_framework import serializers
from photos import models
from django.contrib.auth import get_user_model


class ApodPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ApodPhoto
        fields = ('id', 'author', 'date', 'title', 'url', 'explanation', 'media')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')