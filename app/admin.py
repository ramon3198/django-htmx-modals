from django.contrib import admin
from .models import *


class vlanAdmin(admin.ModelAdmin):
    list_display = ('vlan_id', 'name', 'ip','created_at')
admin.site.register(vlanModel,vlanAdmin)
    

