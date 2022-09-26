from django.shortcuts import render
from ref21_app.models import Playlist
from django.http import JsonResponse

def playlist(request):
    playlists = Playlist.objects.all()
    data = {'Playlist' : list(playlists.values())}
    return JsonResponse(data)


def playlist_detail(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    playlist_theme = playlist.Theme.theme
    data = {
        'PlaylistID' : playlist.PlaylistID,
        'PlaylistName' : playlist.PlaylistName,
        'Description' : playlist.Description,
        'PlaylistPosterLocation' : playlist.PlaylistPosterLocation,
        'Theme': playlist_theme
    }
    return JsonResponse(data)

