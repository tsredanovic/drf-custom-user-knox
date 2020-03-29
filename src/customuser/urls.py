from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# API patterns
api_patterns = [
    url(r'^api/v1/', include('users.api.urls')),
    url(r'^api/v1/', include('examples.api.urls')),
]

# Swagger configuration
schema_view = get_schema_view(
    info=openapi.Info(
        title="Custom user API",
        default_version='v1',
        contact=openapi.Contact(email="toni.sredanovic@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=api_patterns
)

# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + api_patterns

# Media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
