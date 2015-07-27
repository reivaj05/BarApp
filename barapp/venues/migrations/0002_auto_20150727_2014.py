# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='image',
            field=models.ImageField(default=b'/static/venues/img/venue_photo.png', upload_to=b'', blank=True, help_text='Upload an image for the venue', verbose_name='Image venue'),
        ),
    ]
