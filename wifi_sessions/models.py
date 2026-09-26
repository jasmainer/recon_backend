from django.db import models
from deposits.models import Deposit


class WiFiSession(models.Model):
    class SessionStatus(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Active'
        PAUSED = 'PAUSED', 'Paused'
        EXPIRED = 'EXPIRED', 'Expired'
        COMPLETED = 'COMPLETED', 'Completed'

    session_code = models.CharField(
        max_length=50,
        unique=True
    )

    deposit = models.ForeignKey(
        Deposit,
        on_delete=models.PROTECT,
        related_name='wifi_sessions'
    )

    mac_address = models.CharField(
        max_length=17
    )

    minutes_allocated = models.PositiveIntegerField(
        default=0
    )

    time_remaining_sec = models.PositiveIntegerField(
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=SessionStatus.choices,
        default=SessionStatus.ACTIVE
    )

    session_start = models.DateTimeField(
        null=True,
        blank=True
    )

    session_end = models.DateTimeField(
        null=True,
        blank=True
    )

    paused_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.session_code