import os
import mimetypes

from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

#from .thumbs import ImageWithThumbsField

def slugify_uniquely(value, obj, slugfield="slug"):
    suffix = 1
    potential = base = slugify(value)
    filter_params = {}
    filter_params['user'] = obj.user
    while True:
        if suffix > 1:
            potential = "-".join([base, str(suffix)])
        filter_params[slugfield] = potential
        obj_count = obj.__class__.objects.filter(**filter_params).count()
        if not obj_count:
            return potential[:50]
        # we hit a conflicting slug, so bump the suffix & try again
        suffix += 1


class Artist(models.Model):
    user = models.OneToOneField(User)

    @receiver(post_save,sender=User)
    def create_user_artist(sender,instance,created,**kwargs):
        if created:
            Artist.objects.create(user=instance)

    @receiver(post_save,sender=User)
    def save_user_artist(sender,instance,**kwargs):
        instance.artist.save()


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Track(models.Model):
    user = models.ForeignKey(Artist,
                             related_name="tracks",blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    audio_file = models.FileField(
        _("Audio file"),upload_to= "audio%Y/%m/%d",blank=True)
    #image = ImageWithThumbsField(
        #_("Image"),upload_to="images%Y/%m/%d",null=True,blank=True,
        #sizes=((80,80),(200,200)))
    title = models.CharField(_("Title"),max_length=200,null=True)
    genre = models.ForeignKey(Genre,null=True,blank=True)
    date = models.CharField(_("Date"),max_length=200,null=True,blank=True)
    description = models.CharField(_("Description"),max_length=255,null=True,blank=True)
    slug = models.SlugField(verbose_name=_("Slug(last part of url)"))
    _original_slug = None

    def __unicode__(self):
        return self.name

    def save(self,**kwargs):
        if not self.slug:
            slug_source = getattr(self,'title') or \
                os.path.splitext(os.path.basename(self.audio_file.name))[0]
            self.slug = slugify_uniquely(slug_source,self)
        super(Track,self).save(**kwargs)

    @property
    def mimetype(self):
        if not hasattr(self, '_mimetype'):
            self._mimetype = mimetypes.guess_type(self.audio_file.path)[0]
        return self._mimetype

    @property
    def filetype(self):
        if '/' in self.mimetype:
            type_names = {'mpeg': 'MP3', 'ogg': 'Ogg Vorbis'}
            filetype = self.mimetype.split('/')[1]
            return type_names.get(filetype, filetype)
        else:
            return self.mimetype






