from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from venues.models import Venue


# Create your models here.


class Menu(models.Model):

    class Meta:
        verbose_name = _('Menu')
        verbose_name_plural = _('Menus')

    name = models.CharField(
        _('menu'),
        max_length=50,
        blank=True,
        help_text=_('Write a name for the menu')
    )  # ??
    description = models.TextField(
        _('description'),
        max_length=255,
        blank=True,
        help_text=_('Write a description for the menu')
    )  # ??
    #venue = models.ForeignKey(Venue, help_text=_('Select the desired venue'))

    def __unicode__(self):
        return '{menu_name}'.format(menu_name=self.name)


class MenuSection(models.Model):

    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')

    name = models.CharField(
        _('Section name'),
        max_length=50,
        help_text=_('Write a name for the menu section')
    )
    description = models.TextField(
        _('Section description'),
        max_length=255,
        blank=True,
        help_text=_('Write a description for the menu section')
    )
    image = models.ImageField(
        _('Image section'),
        blank=True,
        default='{url}{image_path}'.format(
            url=settings.STATIC_URL,
            image_path='menus/img/section_photo.png'),
        help_text=_('Upload an image for the menu section')

    )
    menu = models.ForeignKey(Menu, help_text=_('Select the desired menu'))

    def __unicode__(self):
        return '{section_name}'.format(section_name=self.name)


class Product(models.Model):

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    name = models.CharField(
        _('Product name'),
        max_length=50,
        help_text=_('Write a name for the product')
    )
    description = models.TextField(
        _('Product description'),
        max_length=255,
        blank=True,
        help_text=_('Write a description for the product')
    )
    price = models.DecimalField(
        _('Product price'),
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(1)],
        default=1,
        help_text=_('Write a price for the  product')
    )
    image = models.ImageField(
        _('Image product'),
        blank=True,
        default='{url}{image_path}'.format(
            url=settings.STATIC_URL,
            image_path='menus/img/product_photo.png'),
        help_text=_('Upload an image for the product')
    )
    section = models.ForeignKey(MenuSection, help_text=_('Select the desired section'))

    def __unicode__(self):
        return '{product_name}'.format(product_name=self.name)