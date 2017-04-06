from django.forms import *
from django.contrib.auth.forms import UserCreationForm
from core.models import Profile
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','password1','password2','email')


class ProfileForm(models.ModelForm):
    class Meta:
        model = Profile
        fields=('is_artist',)