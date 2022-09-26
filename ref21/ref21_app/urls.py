from django.urls import path, include
from ref21_app.views import playlist, playlist_detail

urlpatterns = [
    path('list/', playlist, name='play-list'),
    path('<str:pk>', playlist_detail, name='playlist_detail'),
]
