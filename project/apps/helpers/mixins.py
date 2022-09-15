from drf_extended_viewset import ExtendViewSet
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ExtendModelRetrieveViewSetMixin(ExtendViewSet, mixins.RetrieveModelMixin, GenericViewSet):
    pass
