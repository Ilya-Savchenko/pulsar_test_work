from rest_framework import routers

from .views import ProductViewSet, CategoryRetrieveViewSet

router = routers.DefaultRouter()
router.register('product', ProductViewSet, 'product')
router.register('category', CategoryRetrieveViewSet, 'category')
