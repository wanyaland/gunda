from django import forms
from core.models import Track
from django.contrib.auth.forms import UserCreationForm

class TrackUploadForm(forms.ModelForm):
    class Meta:
        model = Track



        