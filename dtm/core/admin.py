from django.contrib import admin
from core.models import MenuItem


@admin.register(MenuItem)
class AdminMenuItem(admin.ModelAdmin):
    list_display = ('title', 'menu_name', 'parent')
    list_filter = ('menu_name',)
