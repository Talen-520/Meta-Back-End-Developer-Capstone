from django.contrib import admin 
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [ 
    #path('', sayHello, name='sayHello'), 
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('bookings/',views.BookingListView.as_view(), name='booking-list'),
    path('bookings/<int:id>/',views.BookingDetailView.as_view(), name='booking-detail'),
]