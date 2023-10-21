from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from settings import translator as _
# Create your models here.

class Product(models.Model):

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ('sorting',)
        permissions = (('export_product', _('Can export')), ('import_product', _('Can import')))


    owner = models.ForeignKey('accounts.Seller', verbose_name=_('Owner'), on_delete=models.CASCADE)
    template = models.ForeignKey('ProductTemplate', verbose_name=_('Template'), blank=True, null=True, on_delete=models.SET_NULL)
    digital = models.BooleanField(_('Is not real product'), default=False)
    visible = models.BooleanField(_('visible'), default=False)
    sorting = models.PositiveSmallIntegerField(_('Sorting'), blank=True, null=True)
    title = models.CharField(_('Title of object'), max_length=255, blank=True, default='', help_text=_('in title html attribute'))
    alt = models.CharField(_('Subtitle of object'), max_length=255, blank=True, default='', help_text=_('in alt html attribute'))
    slug = models.SlugField(_('uri slug of object'), max_length=255, blank=True, default='', help_text=_('uri slug field'))
    description = models.TextField(_('Description'), blank=True, default='')
    images = GenericRelation('core.Image')

    attributes = models.ManyToManyField('Attribute', through='ProductProperty')


class ProductProperty(models.Model):

    class Meta:
        verbose_name = _('Product Property')
        verbose_name_plural = _('Products Properties')

    value = models.CharField(_('Value of property'), max_length=255)  # Title of element
    visible = models.BooleanField(_('visible'), default=False)
    sorting = models.PositiveSmallIntegerField(_('Sorting'), blank=True, null=True)

    attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    additional = models.ForeignKey('Additional', on_delete=models.CASCADE, blank=True, null=True)


class Attribute(models.Model):
    cache_keys = ('filters',)

    class Meta:
        verbose_name = _('Attribute')
        verbose_name_plural = _('Attributes')
        default_related_name = 'attributes'
        ordering = ('sorting',)

    is_filter = models.BooleanField(_('Is filter'), default=False)
    property_type = models.CharField(_('Type of value'),  null=False, max_length=255, default='str',
        choices=(('str', 'str'), ('int', 'int'), ('float', 'float'), ('datetime', 'datetime')))
    visible = models.BooleanField(_('visible'), default=False)
    sorting = models.PositiveSmallIntegerField(_('Sorting'), blank=True, null=True)
    title = models.CharField(_('Title of object'), max_length=255, blank=True, default='', help_text=_('in title html attribute'))
    alt = models.CharField(_('Subtitle of object'), max_length=255, blank=True, default='', help_text=_('in alt html attribute'))
    slug = models.SlugField(_('uri slug of object'), max_length=255, blank=True, default='', help_text=_('uri slug field'))
    description = models.TextField(_('Description'), blank=True, default='')
    images = GenericRelation('core.Image')


class Additional(models.Model):

    class Meta:
        verbose_name = _('Additional Info')
        verbose_name_plural = _('Additional Infos')
        default_related_name = 'additionals'

    title = models.CharField(_('Title of additional info'), max_length=255, blank=True, default='', help_text=_('in title html attribute'))
    alt = models.CharField(_('Subtitle of additional info'), max_length=255, blank=True, default='', help_text=_('in alt html attribute'))
    description = models.TextField(_('Description'), blank=True, default='')
    images = GenericRelation('core.Image')


class ProductTemplate(models.Model):

    class Meta:
        verbose_name = _('Product Template')
        verbose_name_plural = _('Product Templates')
        default_related_name = 'templates'

    title = models.CharField(_('Title of template'), max_length=255, help_text=_('Name of product Template'))
    attributes = models.ManyToManyField('Attribute')
