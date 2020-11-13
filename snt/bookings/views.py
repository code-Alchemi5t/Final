from django.shortcuts import render
from national.models import NBooking
from international.models import IBooking
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from bookings.owner import OwnerUpdateView, OwnerDeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class Bookings(LoginRequiredMixin, View):
    def get(self,request):
        booking_list=NBooking.objects.filter(owner=self.request.user, status="Confirmed")
        booking_list_international=IBooking.objects.filter(owner=self.request.user, status="Confirmed")
        ctx={'booking_list':booking_list, 'booking_list_international':booking_list_international}
        return render(request,'bookings/booking_list.html',ctx)
# Create your views here.

class UpdateNBookings(OwnerUpdateView):
    model=NBooking
    fields=['name','date','any_special_requests','preferred_mode_of_travel']
    template_name= 'bookings/booking_update_form.html'
    success_url=reverse_lazy('bookings:all')

class DeleteNBookings(OwnerDeleteView):
    model=NBooking
    template_name= 'bookings/booking_confirm_delete.html'
    success_url=reverse_lazy('bookings:all')

class UpdateIBookings(OwnerUpdateView):
    model=IBooking
    fields=['name','date','any_special_requests','preferred_mode_of_travel']
    template_name= 'bookings/booking_update_form.html'
    success_url=reverse_lazy('bookings:all')

class DeleteIBookings(OwnerDeleteView):
    model=IBooking
    template_name= 'bookings/booking_confirm_delete.html'
    success_url=reverse_lazy('bookings:all')