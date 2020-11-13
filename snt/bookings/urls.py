from django.urls import path
from . import views

app_name="bookings"
urlpatterns=[
    path('', views.Bookings.as_view(), name='all'),
    path('bookings/<int:pk>/nupdate/', views.UpdateNBookings.as_view(), name='n_booking_update'),
    path('bookings/<int:pk>/ndelete/', views.DeleteNBookings.as_view(), name='n_booking_confirm_delete'),
    path('bookings/<int:pk>/iupdate/', views.UpdateIBookings.as_view(), name='i_booking_update'),
    path('bookings/<int:pk>/idelete/', views.DeleteIBookings.as_view(), name='i_booking_confirm_delete'),
]