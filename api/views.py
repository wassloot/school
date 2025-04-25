
from rest_framework import viewsets
from .models import Room, Booking, Resource
from .serializers import RoomSerializer, BookingSerializer, ResourceSerializer
from .permissions import IsAdminOrOwner
from rest_framework.permissions import IsAuthenticated
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.shortcuts import redirect
from rest_framework import generics


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAdminOrOwner]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Booking.objects.all()
        return Booking.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




def home_view(request):
    return render(request, 'home.html')



def calendar_view(request, resource_id):
    resource = Resource.objects.get(id=resource_id)
    bookings = Booking.objects.filter(resource=resource)
    bookings_json = json.dumps([
        {
            'title': 'Забронировано',
            'start': b.start_time.isoformat(),
            'end': b.end_time.isoformat()
        } for b in bookings
    ], cls=DjangoJSONEncoder)

    return render(request, 'booking/calendar.html', {
        'resource': resource,
        'bookings_json': bookings_json,
    })



def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def booking_list_view(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/booking_list.html', {'bookings': bookings})

def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking/booking_detail.html', {'booking': booking})



def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room/room_list.html', {'rooms': rooms})

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'room/room_detail.html', {'room': room})



def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'resource/resource_list.html', {'resources': resources})

def resource_detail(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    return render(request, 'resource/resource_detail.html', {'resource': resource})



from rest_framework.permissions import AllowAny



class RoomListView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]



@login_required
def profile_view(request):
    return render(request, 'user/profile.html', {'user': request.user})