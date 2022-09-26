from django.contrib import admin
from .models import Theme, Playlist, Video, Country, User, Watchlist, VideoTimePosition
from django.db.models import Count
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.

class ThemeAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(ThemeAdmin, self).get_queryset(request)
        return qs.annotate(playlist_count=Count('playlist'))

    def playlist_count(self, inst):
        return inst.playlist_count
    list_display = ['theme','playlist_count']

class PlaylistAdmin(admin.ModelAdmin):
    search_fields = ['PlaylistName', 'PlaylistID']

    def get_queryset(self, request):
        qs = super(PlaylistAdmin, self).get_queryset(request)
        return qs.annotate(video_count=Count('video'))

    def video_count(self, inst):
        return inst.video_count
    list_display = ['PlaylistName', 'Theme', 'video_count']
    list_display_links = ['PlaylistName', 'Theme']

class VideoAdmin(admin.ModelAdmin):
    autocomplete_fields = ['PlaylistID']
    list_display = ['Name', 'Pembicara', 'PlaylistID']
    list_display_links = ['Name', 'Pembicara']
    search_fields = ['VODID','Name', 'Pembicara']
    list_filter = ['PlaylistID',]
class CountryAdmin(admin.ModelAdmin):
    search_fields = ['CountryCode','CountryName']

class UserAdmin(admin.ModelAdmin):
    search_fields = ['Firstname','Lastname', 'Email', 'Location']
    list_display = ['Firstname','Lastname', 'Email', 'Gender', 'Location', 'CountryCode']
    list_filter = ['CountryCode',]

class WatchlistAdmin(admin.ModelAdmin):
    list_display = ['id','UID', 'VODID']

class VideoTimePositionAdmin(admin.ModelAdmin):
    list_display = ['id','UID', 'VODID','TimePosition']
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = CustomUser
    
    list_display = ('Firstname','Lastname', 'email', 'is_active',
                    'is_staff', 'is_superuser', 'last_login',)
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    list_display_links= ('Firstname','Lastname', 'email')
    fieldsets = (
        (None, {'fields': ( 'id','email', 'Firstname', 'Lastname', 'password', 'Gender', 'Location', 'CountryCode')}),
        ('Permissions', {'fields': ('is_active','is_staff', 
         'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    

admin.site.register(Theme, ThemeAdmin)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Country,CountryAdmin)
#admin.site.register(User, UserAdmin)
admin.site.register(Watchlist, WatchlistAdmin)
admin.site.register(VideoTimePosition, VideoTimePositionAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
def app_resort(func):                                                                                            
    def inner(*args, **kwargs):                                                                                            
        app_list = func(*args, **kwargs)
        # Useful to discover your app and module list:
        #import pprint                                                                                          
        #pprint.pprint(app_list)

        app_sort_key = 'name'
        app_ordering = {
            "ref21_app": 1,
        }

        resorted_app_list = sorted(app_list, key=lambda x: app_ordering[x[app_sort_key]] if x[app_sort_key] in app_ordering else 1000)

        model_sort_key = 'object_name'
        model_ordering = {
            "Theme": 1,
            "Playlist": 2,
            "Video": 3,
            "User": 4,
            "CustomUser": 5,
            "Country": 6,
            "Watchlist" : 7,
            "VideoTimePosition" : 8,
        }
        for app in resorted_app_list:
            app['models'].sort(key=lambda x: model_ordering[x[model_sort_key]] if x[model_sort_key] in model_ordering else 1000)
        return resorted_app_list
    return inner                                                                                            
                   
admin.site.get_app_list = app_resort(admin.site.get_app_list)