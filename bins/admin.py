from django.contrib import admin
from .models import Bin


@admin.register(Bin)
class BinAdmin(admin.ModelAdmin):
    list_display = (
        'bin_code',
        'location_name',
        'fill_level',
        'status',
        'cumulative_waste_grams',
        'last_emptied_at',
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'bin_code',
        'location_name',
    )