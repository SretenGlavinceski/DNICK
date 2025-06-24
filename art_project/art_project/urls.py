from django.contrib import admin
from django.urls import path
from art_app import views as art_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', art_views.index, name='index'),
    path('add-exhibition/', art_views.add_exhibition, name='add_exhibition'),
    path('edit-exhibition/<int:id_exhibition>', art_views.edit_exhibition, name='edit_exhibition'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
