from django import forms
from core.models import Track

class TrackUploadForm(forms.ModelForm):
    class Meta:
        model = Track