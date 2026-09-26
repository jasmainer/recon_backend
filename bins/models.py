from django.db import models


class Bin(models.Model):
    class BinStatus(models.TextChoices):
        READY = 'READY', 'Ready'
        FULL = 'FULL', 'Full'

    bin_code = models.CharField(max_length=50, unique=True)
    location_name = models.CharField(max_length=150)

    fill_level = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=10,
        choices=BinStatus.choices,
        default=BinStatus.READY
    )

    last_emptied_at = models.DateTimeField(
        null=True,
        blank=True
    )

    cumulative_waste_grams = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.bin_code} - {self.location_name}"