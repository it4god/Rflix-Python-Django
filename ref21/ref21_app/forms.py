from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'Firstname', 'Lastname', 'Gender','Location','CountryCode',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'Firstname', 'Lastname', 'Gender','Location','CountryCode',)