from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers

from apps.goods.urls import router as good_router

router = routers.DefaultRouter()
router.registry.extend(good_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include((router.urls, "api-root")), name="api-root"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

]
