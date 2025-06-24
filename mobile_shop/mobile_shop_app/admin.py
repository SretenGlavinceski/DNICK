from django.contrib import admin
from .models import *


class MobileAdmin(admin.ModelAdmin):
    exclude = ('user', )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(MobileAdmin, self).save_model(request, obj, form, change)


admin.site.register(Manufacturer)
admin.site.register(Mobile, MobileAdmin)