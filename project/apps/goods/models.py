from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from transliterate import translit

from apps.helpers.models import TitleModel, CreatedModel, UpdatedModel, UrlCodeModel


class PropertyObject(TitleModel, CreatedModel, UpdatedModel, UrlCodeModel):
    class TypeChoice(models.TextChoices):
        STRING = ("string", _("String"))
        NUMBER = ("number", _("Number"))

    type = models.CharField(max_length=6, choices=TypeChoice.choices)

    def __str__(self):
        return self.title


class Category(TitleModel, CreatedModel, UpdatedModel):
    slug = models.SlugField(max_length=256, null=True, blank=True)
    properties = models.ManyToManyField(to=PropertyObject, related_name='categories')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(translit(self.title, language_code='ru', reversed=True))

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Product(TitleModel, CreatedModel, UpdatedModel):
    slug = models.SlugField(max_length=256, null=True, blank=True)
    sku = models.CharField(max_length=30, unique=True, verbose_name=_("Vendor code"))
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='products')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(translit(self.title, language_code='ru', reversed=True))
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}, sku: {self.sku}'


class PropertyValue(UrlCodeModel):
    type_str = models.CharField(max_length=15, null=True, blank=True)
    type_number = models.CharField(max_length=15, null=True, blank=True)
    property_obj = models.ForeignKey(to=PropertyObject, on_delete=models.CASCADE, related_name='property_value')
    products = models.ManyToManyField(to=Product, related_name='property_values')

    def __str__(self):
        return self.code
