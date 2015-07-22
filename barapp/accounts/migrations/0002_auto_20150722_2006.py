# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image_profile',
            field=models.ImageField(default=b'/static/accounts/img/profile-photo.png', upload_to=accounts.models.get_file_path, blank=True, help_text='Upload an image for the user profile', verbose_name='User image profile'),
        ),
    ]
