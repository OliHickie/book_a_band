from django.contrib import admin
from .models import Category, Band


class BandAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'tagline',
        'price',
        'location',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    ordering = ('name',)


admin.site.register(Band, BandAdmin)
admin.site.register(Category, CategoryAdmin)
