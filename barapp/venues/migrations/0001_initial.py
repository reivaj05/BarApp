# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Write a name for the venue', unique=True, max_length=50, verbose_name='Venue name')),
                ('description', models.TextField(help_text='Write a description for the venue', max_length=255, verbose_name='Description', blank=True)),
                ('direction', models.TextField(help_text='Write a direction for the venue', max_length=150, verbose_name='Direction', blank=True)),
                ('phone_number', models.CharField(help_text='Write a phone number for the venue', max_length=15, verbose_name='Phone number', blank=True)),
                ('image', models.ImageField(default=b'/static/menus/img/venue_photo.png', upload_to=b'', blank=True, help_text='Upload an image for the venue', verbose_name='Image venue')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Venue',
                'verbose_name_plural': 'Venues',
            },
            bases=(models.Model,),
        ),
    ]
