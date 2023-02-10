from drf_spectacular.views import (
    SpectacularAPIView,
    SpectaculareSwaggerView,
)
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/',SpectacularAPIView.as_view(),name='api-schema'),
    path(
        'api/docs/',
        SpectaculareSwaggerView.as_view(url_name='api-chema'),
        name='api-docs',
    )
]
