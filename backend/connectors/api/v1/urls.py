from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors135617ViewSet

router = DefaultRouter()
router.register(
    "testconnectors135617", Testconnectors135617ViewSet, basename="testconnectors135617"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
