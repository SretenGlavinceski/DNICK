from django.contrib import admin
from .models import *
from datetime import datetime


class ExhibitionAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        artist = Artist.objects.filter(user=request.user).first()
        if artist:
            return Exhibition.objects.filter(artwork__artist=artist).distinct()

        if request.user.is_superuser:
            return Exhibition.objects.filter(date_start__gt=datetime.now().date()).all()

        return Exhibition.objects.none()

    def has_add_permission(self, request):
        return request.user.is_superuser


class ArtistAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser


class ArtWorkAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.artist = Artist.objects.filter(user=request.user).first()
        super(ArtWorkAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return Artist.objects.filter(user=request.user).exists()

    def has_change_permission(self, request, obj=None):
        return obj and obj.artist.user == request.user


admin.site.register(Exhibition, ExhibitionAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(ArtWork, ArtWorkAdmin)
