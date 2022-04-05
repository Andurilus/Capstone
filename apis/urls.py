from django.urls import path

from . import views

urlpatterns = [
    path('apod/', views.ApodList.as_view()),
    path('apod/<int:pk>', views.ApodDetail.as_view()),
    path('currentuser/', views.CurrentUserView.as_view()),
]
