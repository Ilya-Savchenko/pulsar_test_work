from django.utils.translation import gettext as _
from drf_extended_viewset import ExtendedModelViewSet
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import AllowAny

from apps.goods.filters import ProductFilter
from apps.goods.models import Product, Category
from apps.goods.serializers import (
    ProductSerializer,
    ProductListSerializer,
    ProductRetrieveSerializer,
    ProductUpdateSerializer,
    CategorySerializer,
)
from apps.helpers.mixins import ExtendModelRetrieveViewSetMixin


@extend_schema_view(
    create=extend_schema(description=_('Create new product.')),
    list=extend_schema(description=_('List of all products.')),
    retrieve=extend_schema(description=_('Get product by id.')),
    update=extend_schema(description=_('Full update product.')),
    partial_update=extend_schema(description=_('Partial update product.')),
    destroy=extend_schema(description=_('Delete product.')),
)
class ProductViewSet(ExtendedModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    serializer_class_map = {
        'create': ProductSerializer,
        'list': ProductListSerializer,
        'retrieve': ProductRetrieveSerializer,
        'update': ProductUpdateSerializer,
        'partial_update': ProductUpdateSerializer,
    }
    permission_classes = (AllowAny,)
    permission_classes_map = {
        'create': AllowAny,
        'list': AllowAny,
        'retrieve': AllowAny,
        'update': AllowAny,
        'partial_update': AllowAny,
        'destroy': AllowAny,
    }

    def get_serializer_class(self):
        category_id = self.request.query_params.get('category')
        if self.action == 'list' and category_id is not None:
            return ProductRetrieveSerializer
        return super().get_serializer_class()


@extend_schema_view(retrieve=extend_schema(description=_('Get category by id.')), )
class CategoryRetrieveViewSet(ExtendModelRetrieveViewSetMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    serializer_class_map = {
        'retrieve': CategorySerializer,
    }
    permission_classes = (AllowAny,)
