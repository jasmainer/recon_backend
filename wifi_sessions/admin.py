from django.contrib import admin
from .models import WiFiSession


@admin.register(WiFiSession)
class WiFiSessionAdmin(admin.ModelAdmin):
    list_display = (
        'session_code',
        'deposit',
        'mac_address',
        'minutes_allocated',
        'time_remaining_sec',
        'status',
        'session_start',
        'session_end',
    )

    list_filter = (
        'status',
        'created_at',
    )

    search_fields = (
        'session_code',
        'mac_address',
        'deposit__deposit_code',
    )