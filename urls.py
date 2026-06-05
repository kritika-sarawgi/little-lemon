from django.urls import path

from .views import (
    home,
    MenuItemsView,
    SingleMenuItemView,
    BookingView,
    SingleBookingView
)

urlpatterns = [
    path('', home, name='home'),

    path(
        'menu/',
        MenuItemsView.as_view(),
        name='menu-items'
    ),

    path(
        'menu/<int:pk>/',
        SingleMenuItemView.as_view(),
        name='single-menu-item'
    ),

    path(
        'booking/tables/',
        BookingView.as_view(),
        name='booking-list'
    ),

    path(
        'booking/tables/<int:pk>/',
        SingleBookingView.as_view(),
        name='single-booking'
    ),
]