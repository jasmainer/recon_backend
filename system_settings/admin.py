from django.contrib import admin
from .models import SystemSetting


@admin.register(SystemSetting)
class SystemSettingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'minimum_deposit_grams',
        'maximum_minutes_per_transaction',
        'session_expiry_hours',
        'bin_fill_alert_threshold',
        'updated_at',
    )