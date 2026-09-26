from rest_framework import serializers
from .models import WiFiSession


class WiFiSessionSerializer(serializers.ModelSerializer):
    deposit_code = serializers.CharField(
        source='deposit.deposit_code',
        read_only=True
    )

    class Meta:
        model = WiFiSession
        fields = [
            'id',
            'session_code',
            'deposit',
            'deposit_code',
            'mac_address',
            'minutes_allocated',
            'time_remaining_sec',
            'status',
            'session_start',
            'session_end',
            'paused_at',
            'created_at',
            'updated_at',
        ]