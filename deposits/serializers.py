from rest_framework import serializers
from .models import Deposit


class DepositSerializer(serializers.ModelSerializer):
    bin_code = serializers.CharField(
        source='bin.bin_code',
        read_only=True
    )

    class Meta:
        model = Deposit
        fields = [
            'id',
            'deposit_code',
            'bin',
            'bin_code',
            'weight_grams',
            'status',
            'minutes_earned',
            'created_at',
        ]