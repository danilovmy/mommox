from django.contrib import admin
from .models import Product, Attribute, Additional, ProductTemplate


class PropertyInline(admin.TabularInline):
    model = Product.attributes.through
    extra = 0


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    inlines = [PropertyInline]
    ...

@admin.register(Attribute)
class AttributeModelAdmin(admin.ModelAdmin):
    ...

@admin.register(Additional)
class AdditionalModelAdmin(admin.ModelAdmin):
    ...


@admin.register(ProductTemplate)
class ProductTemplateModelAdmin(admin.ModelAdmin):
    ...
