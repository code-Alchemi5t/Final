from django.urls import path, reverse_lazy
from . import views

app_name="national"
urlpatterns=[
    path('', views.NewBookingCreate.as_view(), name='all'),
    path('national/<int:pk>', views.ConfirmBooking.as_view(), name='confirm_booking'),
    path('national/<int:pk>/delete', views.NewBookingDeleteView.as_view(success_url=reverse_lazy('national:all')), name='newbooking_delete'),
]