
from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext as _
from .managers import CustomUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
# Create your models here.

class Theme(models.Model):
    theme = models.CharField(max_length=100)
    
    def __str__(self):
        return self.theme
    
class Playlist(models.Model):
    PlaylistID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    PlaylistName = models.CharField(max_length=255)
    Description = models.TextField()
    PlaylistPosterLocation = models.CharField(max_length=255)
    Theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

    def __str__(self):
            return self.PlaylistName

class Video(models.Model):
    VODID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    Name = models.CharField(max_length=255)
    Pembicara = models.CharField(max_length=255)
    VideoLength = models.CharField(max_length=30)
    Playlist_Master_Location = models.CharField(max_length=255)
    Playlist_360p_Location = models.CharField(max_length=255)
    Playlist_480p_Location = models.CharField(max_length=255)
    Playlist_720p_Location = models.CharField(max_length=255)
    Playlist_1080p_Location = models.CharField(max_length=255)
    Description = models.TextField()
    PlaylistID = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    PosterLocation = models.CharField(max_length=255)
    TimePosition : models.IntegerField(default=0)

    def __str__(self):
            return self.Name
        
class Country(models.Model):
    CountryCode = models.CharField(max_length=2, primary_key=True)
    CountryName = models.CharField(max_length=50)

    def __str__(self):
        return self.CountryName

class User(models.Model):
    UID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=60)
    Gender = models.CharField(max_length=1)
    Location = models.CharField(max_length=100)
    CountryCode = models.ForeignKey(Country, on_delete=models.CASCADE)
    Password =  models.CharField(max_length=200)
    
    def __str__(self):
        return self.Firstname + " " + self.Lastname

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    username = models.CharField(max_length=100)
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    email = models.EmailField(_('email address'), unique=True)
    Gender = models.CharField(max_length=1)
    Location = models.CharField(max_length=100)
    CountryCode = models.ForeignKey(Country, on_delete=models.CASCADE,blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(_('is active'), default=True)
    is_staff = models.BooleanField(_('is staff'), default=True)
    is_superuser = models.BooleanField(_('is superuser'), default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username','Gender', 'Location', 'Firstname', 'Lastname')

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    class Meta:
         verbose_name = "User"
class Watchlist(models.Model):
    UID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    VODID = models.ForeignKey(Video, on_delete=models.CASCADE)

class VideoTimePosition(models.Model):
    UID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    VODID = models.ForeignKey(Video, on_delete=models.CASCADE)
    TimePosition = models.CharField(max_length=15)


