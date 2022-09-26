from django.urls import path, include
#from ref21_app.api.views import playlist, playlist_detail, video, video_detail, video_list, watchlist, watchlistvideo, videotimeposition
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from ref21_app.api.views import PlaylistView, PlaylistVideoView, VideoView, VideoDetailView, WatchlistView, WatchlistVideoView, VideoTimePositionView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('playlist', PlaylistView.as_view(), name='play-list'),
    path('playlist-video/<str:PlaylistID>', PlaylistVideoView.as_view(), name='playlist_video_list-detaillist'),
    path('video-list', VideoView.as_view(), name='video-list'),
    path('video/<str:pk>',VideoDetailView.as_view(), name='video-detail'),
    path('watchlist',WatchlistView.as_view(), name='watchlist'),
    path('watchlistvideo/<str:UID>/<str:VODID>',WatchlistVideoView.as_view(), name='watchlist-video'),
    path('videotimeposition/<str:UID>/<str:VODID>',VideoTimePositionView.as_view(), name='video-time-position')
]
