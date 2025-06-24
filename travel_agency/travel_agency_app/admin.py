from django.contrib import admin
from .models import *
from django.db.models import Sum, Count


class TourGuideAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(TourGuideAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            qs = qs.annotate(num_tours=Count('tours')).filter(num_tours__lte=3)

        return qs

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


class TourAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):

        total_cost = Tour.objects.filter(tour_guide=obj.tour_guide).exclude(id=obj.id).aggregate(Sum('price'))[
            'price__sum']
        new_price = obj.price

        if total_cost + new_price > 50000:
            self.message_user(request, f'Tour guide {obj.tour_guide} will exceed limit of 50K!')
            return

        if Tour.objects.filter(place=obj.place).exists():
            self.message_user(request, f'Destination {obj.place} already exists!')
            return

        if not change:
            if Tour.objects.filter(tour_guide=obj.tour_guide).count() == 5:
                self.message_user(request, f'Tour guide {obj.tour_guide} already has 5 destinations!')
                return

            obj.tour_guide.user = request.user

        super(TourAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return obj and obj.tour_guide.user == request.user


admin.site.register(TourGuide)
admin.site.register(Tour)
