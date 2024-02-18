from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sayHello(request):
 return HttpResponse('Hello World')



def index(request):
    return render(request, 'index.html', {})



from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer 
from django.contrib.auth.models import User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Menu
from .serializers import MenuSerializer

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = 'id'  # or another field that you want to look up the Menu items by


# views.py
from rest_framework import generics
from .models import Booking
from .serializers import BookingSerializer

class BookingListView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    lookup_field = 'id'  # Or the field you're using for lookups
