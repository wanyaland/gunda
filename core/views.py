from django.shortcuts import render


# Create your views here.

def home(request):
    return render('core/index.html')

def artist_lists(request):
    return render('core/artists.html')

def playlist(request):
    return render('core/playlist.html')

