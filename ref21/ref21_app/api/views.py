from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from ref21_app.api.serializers import PlaylistSerializer, VideoSerializer, WatchlistSerializer, VideoTimePositionSerializer
from ref21_app.models import Playlist, Video, Watchlist, VideoTimePosition
from django.http import JsonResponse

class PlaylistView(APIView):
#    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        playlists = Playlist.objects.all()
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        playlists = Playlist.objects.all()
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)

class PlaylistVideoView(APIView):
#   permission_classes = (IsAuthenticated,)
    def get(self, request, PlaylistID, format=None):
        videos = Video.objects.all().filter(PlaylistID=PlaylistID)
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

    def post(self, request, PlaylistID, format=None):
        videos = Video.objects.all().filter(PlaylistID=PlaylistID)
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

class VideoView(APIView):
#    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

class VideoDetailView(APIView):
#    permission_classes = (IsAuthenticated,)
    def get(self, request, pk, format=None):
        video= Video.objects.get(pk=pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data)
    def post(self, request, pk, format=None):
        video= Video.objects.get(pk=pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data) 

class WatchlistView(APIView):
#    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        watchlists = Watchlist.objects.all()
        serializer = WatchlistSerializer(watchlists, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        watchlists = Watchlist.objects.all()
        serializer = WatchlistSerializer(watchlists, many=True)
        return Response(serializer.data)
    
class WatchlistVideoView(APIView):
#    permission_classes = (IsAuthenticated,)
    def get(self, request, UID,VODID, format=None):
        if request.method == "GET":
            watchlists = Watchlist.objects.all().filter(UID=UID, VODID=VODID)
            if watchlists:
                serializer = WatchlistSerializer(watchlists, many=True)
                return Response(serializer.data)
            else:
                return Response({"Message ": "Empty Rows"})
    def post(self, request, UID,VODID, format=None):
        watchlists = Watchlist.objects.all().filter(UID=UID, VODID=VODID)
        if watchlists:
            serializer = WatchlistSerializer(watchlists, many=True)
            return Response(serializer.data)
        else:
            serializer = WatchlistSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
    def delete(self, request, UID,VODID, format=None):
        watchlists  = Watchlist.objects.all().filter(UID=UID, VODID=VODID)
        watchlists.delete()
        return Response({"Message": "Deleted!"})
    
class VideoTimePositionView(APIView):
#    permission_classes = (IsAuthenticated,)
    def get(self, request, UID,VODID, format=None):
        videotimepositions = VideoTimePosition.objects.all().filter(UID=UID, VODID=VODID)
        if videotimepositions:
            serializer = VideoTimePositionSerializer(videotimepositions, many=True)
            return Response(serializer.data)
        else:
            return Response({"Message ": "Empty Rows"})
    def post(self, request, UID,VODID, format=None):
        videotimepositions = VideoTimePosition.objects.all().filter(UID=UID, VODID=VODID)
        if videotimepositions:
            serializer = VideoTimePositionSerializer(videotimepositions, many=True)
            return Response(serializer.data)
        else:
            serializer = VideoTimePositionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, UID,VODID, format=None):
        videotimepositions = VideoTimePosition.objects.all().filter(UID=UID, VODID=VODID).first()
        serializer = VideoTimePositionSerializer(videotimepositions, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, UID,VODID, format=None):
        videotimepositions  = VideoTimePosition.objects.all().filter(UID=UID, VODID=VODID)
        videotimepositions.delete()
        return Response({"Message": "Deleted!"})
"""





@api_view(['GET','PUT','POST','DELETE'])
def videotimeposition(request, UID,VODID):
    if request.method == "GET":
        videotimepositions = VideoTimePosition.objects.all().filter(UID=UID, VODID=VODID).first()
        if videotimepositions:
            serializer = VideoTimePositionSerializer(videotimepositions, many=True)
            return Response(serializer.data)
        else:
            return Response({"Empty Rows": ""})
    if request.method == "POST":
        videotimepositions = VideoTimePosition.objects.all().filter(UID=UID, VODID=VODID).first()
        if videotimepositions:
            serializer = VideoTimePositionSerializer(videotimepositions, many=True)
            return Response(serializer.data)
        else:
            serializer = VideoTimePositionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "PUT":
        videotimepositions = VideoTimePosition.objects.all().filter(UID=UID, VODID=VODID).first()
        serializer = VideoTimePositionSerializer(videotimepositions, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    if request.method == "DELETE":
        videotimepositions  = VideoTimePosition.objects.all().filter(UID=UID, VODID=VODID)
        videotimepositions.delete()
        return Response({"Delete": ""})
"""

"""
@api_view(['GET','POST'])
def playlist(request):
    playlists = Playlist.objects.all()
    serializer = PlaylistSerializer(playlists, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def playlist_detail(request,pk):
    playlist= Playlist.objects.get(pk=pk)
    serializer = PlaylistSerializer(playlist)
    return Response(serializer.data)

@api_view(['GET','POST'])
def video(request):
    videos = Video.objects.all()
    serializer = VideoSerializer(videos, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def video_list(request, PlaylistID):
    videos = Video.objects.all().filter(PlaylistID=PlaylistID)
    serializer = VideoSerializer(videos, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def watchlist(request):
    watchlists = Watchlist.objects.all()
    serializer = WatchlistSerializer(watchlists, many=True)
    return Response(serializer.data)

@api_view(['GET','POST','DELETE'])
def watchlistvideo(request, UID,VODID):
    if request.method == "GET":
        watchlists = Watchlist.objects.all().filter(UID=UID, VODID=VODID)
        if watchlists:
            serializer = WatchlistSerializer(watchlists, many=True)
            return Response(serializer.data)
        else:
            return Response({"Empty Rows": ""})
    if request.method == "POST":
        watchlists = Watchlist.objects.all().filter(UID=UID, VODID=VODID)
        if watchlists:
            serializer = WatchlistSerializer(watchlists, many=True)
            return Response(serializer.data)
        else:
            serializer = WatchlistSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
    
    if request.method == "DELETE":
        watchlists  = Watchlist.objects.all().filter(UID=UID, VODID=VODID)
        watchlists.delete()
        return Response({"Delete": ""})

"""