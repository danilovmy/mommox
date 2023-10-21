from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from settings import translator as _


class ContentTyped(models.Model):
    """Base abstract class to define fields for model, which has Generic related Object."""

    class Meta:
        abstract = True

    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING, blank=True, null=True)
    object_id = models.CharField(_('Sourced object id'), max_length=50, blank=True, null=True)

    content_object = GenericForeignKey('content_type', 'object_id')


class Image(ContentTyped, models.Model):

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    title = models.CharField(_('Title of image'), max_length=255, blank=True, default='', help_text=_('in title html attribute'))
    alt = models.CharField(_('Alternative of image'), max_length=255, blank=True, default='', help_text=_('in alt html attribute'))
    image = models.ImageField(verbose_name=_('Image'), upload_to='products')
    sorting = models.PositiveSmallIntegerField(_('Sorting of Image'), blank=True, null=True)
