from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from mobile_shop_app import views as mobile_shop_app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', mobile_shop_app_views.index, name='index'),
    path('product/<int:id_mobile>', mobile_shop_app_views.view_details, name='view_details'),
    path('newProduct/create/', mobile_shop_app_views.create, name='create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
