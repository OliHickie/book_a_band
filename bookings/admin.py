from django.contrib import admin
from .models import NewBooking


class BookingAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'wedding_date',
                    'venue_name', 'email', 'contact_number',)

    ordering = ('wedding_date',)


admin.site.register(NewBooking, BookingAdmin)
