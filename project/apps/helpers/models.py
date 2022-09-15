from django.db import models
from django.utils.translation import gettext_lazy as _


class TitleModel(models.Model):
    title = models.CharField(max_length=256, verbose_name=_("Name"))

    class Meta:
        abstract = True


class CreatedModel(models.Model):
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)

    class Meta:
        abstract = True


class UpdatedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class UrlCodeModel(models.Model):
    code = models.CharField(max_length=15)

    class Meta:
        abstract = True
