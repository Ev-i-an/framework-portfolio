from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path('', include('blog_generator.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.index_title = "Gestion Administrateur"
admin.site.site_header = "Section Administrateur"
admin.site.site_title = "Administration"

