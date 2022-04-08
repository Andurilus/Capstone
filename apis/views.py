from rest_framework import generics

from photos import models
from .serializers import ApodPhotoSerializer, MarsPhotoSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ApodList(generics.ListCreateAPIView):
    queryset = models.ApodPhoto.objects.all()
    serializer_class = ApodPhotoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']

class ApodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ApodPhoto.objects.all()
    serializer_class = ApodPhotoSerializer

class MarsList(generics.ListCreateAPIView):
    queryset = models.MarsPhoto.objects.all()
    serializer_class = MarsPhotoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']

class MarsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MarsPhoto.objects.all()
    serializer_class = MarsPhotoSerializer

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user