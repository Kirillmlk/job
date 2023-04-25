from django.contrib import admin


from django.contrib import admin
from .models import MenuItem, Menu


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'url', 'named_url')


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Menu, MenuAdmin)