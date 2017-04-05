# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.thumbs


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='track',
            name='album',
            field=models.ForeignKey(blank=True, to='core.Album', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='track',
            name='image',
            field=core.thumbs.ImageWithThumbsField(null=True, upload_to=b'images%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
    ]
