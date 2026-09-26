from django.db import models
from bins.models import Bin


class Deposit(models.Model):
    class DepositStatus(models.TextChoices):
        VALID = 'VALID', 'Valid'
        INVALID = 'INVALID', 'Invalid'
        TOO_LIGHT = 'TOO_LIGHT', 'Too Light'

    deposit_code = models.CharField(
        max_length=50,
        unique=True
    )

    bin = models.ForeignKey(
        Bin,
        on_delete=models.PROTECT,
        related_name='deposits'
    )

    weight_grams = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=DepositStatus.choices
    )

    minutes_earned = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.deposit_code