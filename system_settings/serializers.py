from rest_framework import serializers
from .models import SystemSetting


class SystemSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetting
        fields = [
            'id',
            'minimum_deposit_grams',
            'tier_one_max_grams',
            'tier_one_multiplier',
            'tier_two_max_grams',
            'tier_two_base_minutes',
            'tier_two_multiplier',
            'maximum_minutes_per_transaction',
            'session_expiry_hours',
            'bin_fill_alert_threshold',
            'updated_at',
        ]