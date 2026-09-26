from rest_framework import serializers
from .models import Bin


class BinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bin
        fields = [
            'id',
            'bin_code',
            'location_name',
            'fill_level',
            'status',
            'last_emptied_at',
            'cumulative_waste_grams',
            'created_at',
            'updated_at',
        ]