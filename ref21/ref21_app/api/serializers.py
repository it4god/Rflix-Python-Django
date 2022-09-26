from rest_framework import serializers
from ref21_app.models import Playlist, Video, Watchlist, CustomUser, VideoTimePosition

class PlaylistSerializer(serializers.Serializer):
    PlaylistID = serializers.CharField(read_only=True)
    PlaylistName = serializers.CharField(read_only=True)
    Description = serializers.CharField(read_only=True)
    PlaylistPosterLocation = serializers.CharField(read_only=True)
    Theme = serializers.CharField(read_only=True)

class VideoSerializer(serializers.Serializer):
    VODID = serializers.CharField(read_only=True)
    Name = serializers.CharField(read_only=True)
    Pembicara = serializers.CharField(read_only=True)
    VideoLength = serializers.CharField(read_only=True)
    Playlist_Master_Location = serializers.CharField(read_only=True)
    Playlist_360p_Location = serializers.CharField(read_only=True)
    Playlist_480p_Location = serializers.CharField(read_only=True)
    Playlist_720p_Location = serializers.CharField(read_only=True)
    Playlist_1080p_Location = serializers.CharField(read_only=True)
    Description = serializers.CharField(read_only=True)
    PlaylistID = serializers.PrimaryKeyRelatedField(queryset=Playlist.objects.all(),many=False)
    PosterLocation = serializers.CharField(read_only=True)
    TimePosition : serializers.CharField(read_only=True)
    
class WatchlistSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    UID = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(),many=False)
    VODID = serializers.PrimaryKeyRelatedField(queryset=Video.objects.all(),many=False)

    def create(self, validated_data):
        return Watchlist.objects.create(**validated_data)
    
class VideoTimePositionSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    UID = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(),many=False)
    VODID = serializers.PrimaryKeyRelatedField(queryset=Video.objects.all(),many=False)
    TimePosition = serializers.CharField(read_only=False)
    
    def create(self, validated_data):
        return VideoTimePosition.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.UID =  validated_data.get("UID")
        instance.VODID =  validated_data.get("VODID")
        instance.TimePosition = validated_data.get("TimePosition")
        instance.save()
        return instance