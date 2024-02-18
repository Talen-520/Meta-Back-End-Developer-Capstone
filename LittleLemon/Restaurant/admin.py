from django.contrib import admin
from .models import Booking, Menu  # Make sure to import your models

# Define custom admin classes if needed
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'no_of_guests', 'booking_date')  # Customize list display
    search_fields = ('name',)  # Add search functionality

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'inventory')
    list_filter = ('price',)  # Add filter options
    search_fields = ('title',)

# Register your models with custom admin classes
admin.site.register(Booking, BookingAdmin)
admin.site.register(Menu, MenuAdmin)