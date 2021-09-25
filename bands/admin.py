from django.contrib import admin
from .models import Category, Band, BandReview


class BandAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'location',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    ordering = ('name',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'band',
        'name',
        'date_added',
    )

    ordering = ('date_added',)


admin.site.register(Band, BandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BandReview, ReviewAdmin)
