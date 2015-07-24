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
            name='name',
            field=models.CharField(help_text='Write a name for the venue', unique=True, max_length=50, verbose_name='Venue name'),
        ),
    ]
