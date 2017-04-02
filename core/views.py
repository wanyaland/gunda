from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request,'core/index.html')

def artist_lists(request):
    return render(request,'core/artists.html')

def playlist(request):
    return render(request,'core/playlist.html')

