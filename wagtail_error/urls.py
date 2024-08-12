from django.contrib import admin
from django.urls import path, include
from wagtail.admin import urls as wagtailadmin_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("wagtail_admin/", include(wagtailadmin_urls)),
] + static(
        f"{settings.MEDIA_URL}",
        document_root=f"{settings.MEDIA_ROOT}",
    ) + static(
        f"{settings.STATIC_URL}",
        document_root=f"{settings.STATIC_ROOT}",
    )
