# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Write a name for the menu', max_length=50, verbose_name='menu', blank=True)),
                ('description', models.TextField(help_text='Write a description for the menu', max_length=255, verbose_name='description', blank=True)),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Write a name for the menu section', max_length=50, verbose_name='Section name')),
                ('description', models.TextField(help_text='Write a description for the menu section', max_length=255, verbose_name='Section description', blank=True)),
                ('image', models.ImageField(default=b'/static/menus/img/section_photo.png', upload_to=b'', blank=True, help_text='Upload an image for the menu section', verbose_name='Image section')),
                ('menu', models.ForeignKey(help_text='Select the desired menu', to='menus.Menu')),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Write a name for the product', max_length=50, verbose_name='Product name')),
                ('description', models.TextField(help_text='Write a description for the product', max_length=255, verbose_name='Product description', blank=True)),
                ('price', models.DecimalField(decimal_places=2, default=1, max_digits=4, validators=[django.core.validators.MinValueValidator(1)], help_text='Write a price for the  product', verbose_name='Product price')),
                ('image', models.ImageField(default=b'/static/menus/img/product_photo.png', upload_to=b'', blank=True, help_text='Upload an image for the product', verbose_name='Image product')),
                ('section', models.ForeignKey(help_text='Select the desired section', to='menus.MenuSection')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
            bases=(models.Model,),
        ),
    ]
