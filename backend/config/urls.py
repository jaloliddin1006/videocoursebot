from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Eslat Bot API",
        default_version='api',
        description="The Eslat API is helpful for you to manage your time and tasks. You can create your own targets and schedule them. Also, you can create your own daily targets and schedule them. You can find on telegram https://t.me/eslatbek_bot",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="lazy.devsloper@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),
]



if settings.DEBUG:  # new
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
