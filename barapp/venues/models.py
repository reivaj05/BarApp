from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Venue(models.Model):

    class Meta:
        verbose_name = _('Venue')
        verbose_name_plural = _('Venues')

    name = models.CharField(
        _('Venue name'),
        max_length=50,
        unique=True,
        help_text=_('Write a name for the venue')
    )
    description = models.TextField(
        _('Description'),
        max_length=255,
        blank=True,
        help_text=_('Write a description for the venue')
    )
    direction = models.TextField(
        _('Direction'),
        max_length=150,
        blank=True,
        help_text=_('Write a direction for the venue')
    )
    #Change for an appropiate field
    phone_number = models.CharField(
        _('Phone number'),
        max_length=15,
        blank=True,
        help_text=_('Write a phone number for the venue')
    )
    image = models.ImageField(
        _('Image venue'),
        blank=True,
        default='{url}{image_path}'.format(
            url=settings.STATIC_URL,
            image_path='venues/img/venue_photo.png'),
        help_text=_('Upload an image for the venue')
    )
    user = models.ForeignKey(User)

    def __unicode__(self):
        return '{venue_name}'.format(venue_name=self.name)
