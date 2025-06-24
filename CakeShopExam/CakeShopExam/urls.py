from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from CakeShopApp import views as cake_shop_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', cake_shop_views.index, name='index'),
    path('add-cake/', cake_shop_views.add_cake, name='add_cake'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
