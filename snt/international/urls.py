from django.urls import path, reverse_lazy
from . import views

app_name="international"
urlpatterns=[
    path('', views.NewBookingCreate.as_view(), name='all'),
    path('international/<int:pk>', views.ConfirmBooking.as_view(), name='confirm_booking'),
    path('international/<int:pk>/delete', views.NewBookingDeleteView.as_view(success_url=reverse_lazy('international:all')), name='newbooking_delete'),
]