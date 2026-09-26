from django.contrib import admin
from .models import Deposit


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = (
        'deposit_code',
        'bin',
        'weight_grams',
        'status',
        'minutes_earned',
        'created_at',
    )

    list_filter = (
        'status',
        'created_at',
    )

    search_fields = (
        'deposit_code',
        'bin__bin_code',
    )