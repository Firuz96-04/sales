from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    list_display = ('id',)



# @admin.register(HousingClass)
# class AdminHousingClass(admin.ModelAdmin):
#     pass


# @admin.register(BuildingType)
# class AdminBuildingType(admin.ModelAdmin):
#     pass