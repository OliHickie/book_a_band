from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at',)

    ordering = ('updated_at',)


admin.site.register(Blog, BlogAdmin)
