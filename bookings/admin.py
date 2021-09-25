from django.contrib import admin
from .models import NewBooking


class BookingAdmin(admin.ModelAdmin):
    list_display = ('band', 'client_name', 'wedding_date',
                    'venue_name', 'email', 'booking_created_at',
                    'booking_updated_at',)

    ordering = ('wedding_date',)


admin.site.register(NewBooking, BookingAdmin)
