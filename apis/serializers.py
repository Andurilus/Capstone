from rest_framework import serializers
from photos import models
from django.contrib.auth import get_user_model

class NestedApodPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ApodPhoto
        fields = ('id', 'author', 'date', 'title', 'url', 'explanation', 'media')

class NestedMarsPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MarsPhoto
        fields = ('id', 'title', 'sol', 'earth_date', 'date', 'rover', 'camera_name', 'url', 'explanation', 'author')    

class ApodPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ApodPhoto
        fields = ('id', 'author', 'date', 'title', 'url', 'explanation', 'media')

class UserSerializer(serializers.ModelSerializer):
    apodposts = NestedApodPhotoSerializer(read_only=True, many=True)
    marsposts = NestedMarsPhotoSerializer(read_only=True, many=True)
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'apodposts', 'marsposts')

class MarsPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MarsPhoto
        fields = ('id', 'title', 'sol', 'earth_date', 'date', 'rover', 'camera_name', 'url', 'explanation', 'author')