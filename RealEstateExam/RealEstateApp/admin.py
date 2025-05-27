from django.contrib import admin
from .models import *
import datetime


class PropertyAgentInline(admin.TabularInline):
    model = PropertyAgent
    extra = 0


class PropertyCharacteristicsInline(admin.TabularInline):
    model = PropertyCharacteristics
    extra = 0


class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyAgentInline, PropertyCharacteristicsInline, ]
    list_display = ('name', 'area', 'location',)

    def save_model(self, request, obj, form, change):
        super(PropertyAdmin, self).save_model(request, obj, form, change)

        if not change:
            PropertyAgent.objects.create(property=obj, agent=Agent.objects.filter(user=request.user).first())

    def has_add_permission(self, request):
        return Agent.objects.filter(user=request.user).exists()

    def has_delete_permission(self, request, obj=None):
        return obj and not PropertyCharacteristics.objects.filter(property_id=obj.id).exists()

    def has_change_permission(self, request, obj=None):
        curr_agent = Agent.objects.filter(user=request.user).first()
        return obj and PropertyAgent.objects.filter(property_id=obj.id, agent=curr_agent).exists()

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Property.objects.filter(date_released=datetime.date.today()).all()

        return Property.objects.all()


class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname',)
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(AgentAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return request.user.is_superuser


class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)

    def has_add_permission(self, request):
        return request.user.is_superuser


admin.site.register(Property, PropertyAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(PropertyAgent)
admin.site.register(Characteristic, CharacteristicAdmin)
admin.site.register(PropertyCharacteristics)
