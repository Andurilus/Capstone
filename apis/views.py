from rest_framework import generics

from photos import models
from .serializers import ApodPhotoSerializer, UserSerializer

class ApodList(generics.ListCreateAPIView):
    queryset = models.ApodPhoto.objects.all()
    serializer_class = ApodPhotoSerializer

class ApodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ApodPhoto.objects.all()
    serializer_class = ApodPhotoSerializer

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user