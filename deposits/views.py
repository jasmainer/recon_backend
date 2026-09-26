from rest_framework import viewsets
from .models import Deposit
from .serializers import DepositSerializer


class DepositViewSet(viewsets.ModelViewSet):
    queryset = Deposit.objects.all().order_by('-created_at')
    serializer_class = DepositSerializer