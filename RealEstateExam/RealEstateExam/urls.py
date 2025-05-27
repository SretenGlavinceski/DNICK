from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from RealEstateApp import views as real_estate_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', real_estate_views.index, name='index'),
    path('edit-property/<int:id_property>', real_estate_views.edit_property, name='edit_property'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
