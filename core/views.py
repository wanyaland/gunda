from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from forms import TrackUploadForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from core.models import Profile,Genre,Album,Playlist,Track


def home(request):
    tracks = Track.objects.all()
    return render(request,'core/index.html')


def artist_lists(request):
    return render(request,'core/artists.html')


def artist_detail(request,pk):
    artist = get_object_or_404(Profile,pk=pk)
    return render(request,'core/specific-artist.html',{
        'artist':artist,
    })


def playlist(request):
    playlists = Playlist.objects.all()
    return render(request,'core/playlist.html')

def whats_new(request):
    return render(request,'core/new.html')


@login_required
def upload(request):
    state=''
    genres = Genre.objects.all()
    albums = Album.objects.all()
    if request.POST:
        form = TrackUploadForm(request.POST,request.FILES)
        if form.is_valid():
            if request.user.profile.is_artist is False:
                form.save()
                return HttpResponseRedirect(reverse('core:artist_detail', args=(request.user.profile.pk,)))
    else:
        form = TrackUploadForm()
    return render(request,'core/upload.html',{
        'form':form,'state':state,'genres':genres,'albums':albums
    })

