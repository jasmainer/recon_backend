from django.db import models


class SystemSetting(models.Model):
    minimum_deposit_grams = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=5
    )

    tier_one_max_grams = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=20
    )

    tier_one_multiplier = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=3
    )

    tier_two_max_grams = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=50
    )

    tier_two_base_minutes = models.PositiveIntegerField(
        default=60
    )

    tier_two_multiplier = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=2
    )

    maximum_minutes_per_transaction = models.PositiveIntegerField(
        default=480
    )

    session_expiry_hours = models.PositiveIntegerField(
        default=24
    )

    bin_fill_alert_threshold = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=90
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return "RECon System Settings"