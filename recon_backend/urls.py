from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bins.views import BinViewSet
from deposits.views import DepositViewSet
from wifi_sessions.views import WiFiSessionViewSet
from system_settings.views import SystemSettingViewSet


router = DefaultRouter()

router.register(
    r'bins',
    BinViewSet,
    basename='bin'
)

router.register(
    r'deposits',
    DepositViewSet,
    basename='deposit'
)

router.register(
    r'wifi-sessions',
    WiFiSessionViewSet,
    basename='wifi-session'
)

router.register(
    r'settings',
    SystemSettingViewSet,
    basename='system-setting'
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        'api/',
        include(router.urls)
    ),
]