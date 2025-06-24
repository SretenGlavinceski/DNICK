from django.contrib import admin
from .models import *


class CakeAdmin(admin.ModelAdmin):
    exclude = ('baker', )

    def save_model(self, request, obj, form, change):

        if not change and Cake.objects.filter(baker__user=request.user).count() == 10:
            self.message_user(request, f'Baker {obj.baker} already has 10 cakes!')
            return

        total_price = 0
        for cake in Cake.objects.filter(baker__user=request.user).exclude(id=obj.id).all():
            if cake.price:
                total_price += cake.price

        if total_price + obj.price > 10000:
            self.message_user(request, f'Baker {obj.baker} cakes exceed limit of 10K!')
            return

        if not change and Cake.objects.filter(name=obj.name).exists():
            self.message_user(request, f'Cake with name {obj.name} already exists!')
            return

        if not change:
            obj.baker = Baker.objects.filter(user=request.user).first()

        super(CakeAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return obj and obj.baker and obj.baker.user == request.user


class BakerAdmin(admin.ModelAdmin):
    exclude = ('user', )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(BakerAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        if request.user.is_superuser:
            id_bakers = []
            for curr_baker in Baker.objects.all():
                count_baker = Cake.objects.filter(baker=curr_baker).count()
                if count_baker < 5:
                    id_bakers.append(curr_baker.id)

            return Baker.objects.filter(id__in=id_bakers).all()

        return Baker.objects.all()

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser


admin.site.register(Baker, BakerAdmin)
admin.site.register(Cake, CakeAdmin)
