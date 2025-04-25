from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


from .views import RoomViewSet, BookingViewSet, ResourceViewSet

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'resource', ResourceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('bookings/', views.booking_list_view, name='booking_list'),
    path('bookings/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/<int:room_id>/', views.room_detail, name='room_detail'),
    path('resources/', views.resource_list, name='resource_list'),
    path('resources/<int:resource_id>/', views.resource_detail, name='resource_detail'),
    path('profile/', views.profile_view, name='profile'),
]

