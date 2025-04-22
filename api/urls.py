from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import RoomViewSet, BookingViewSet, ResourceViewSet

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'resource', ResourceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]