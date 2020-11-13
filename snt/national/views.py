# Create your views here.
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from national.owner import OwnerDeleteView, OwnerUpdateView
from django.urls import reverse
from national.forms import CreateForm
from national.models import NBooking, NPrice
from django.shortcuts import render, redirect


class NewBookingDeleteView(OwnerDeleteView):
    model = NBooking
    success_url='national:all'
    template_name = 'national/booking_confirm_delete.html'


class NewBookingCreate(LoginRequiredMixin, View):
    template_name='national/booking_form.html'
    success_url='national:all'
    def get(self,request,pk=None):
        form=CreateForm()
        ctx={'form':form}
        return render(request,self.template_name,ctx)

    def post(self,request,pk=None):
        form=CreateForm(request.POST)
        if not form.is_valid():
            ctx={'form':form}
            return render(request,self.template_name,ctx)

        booking=form.save(commit=False)
        booking.owner=self.request.user
        booking.save()
        return redirect(reverse('national:confirm_booking', args=[booking.id]))


class ConfirmBooking(LoginRequiredMixin, View):
    def get(self,request,pk):
        booking=NBooking.objects.get(id=pk)
        y=NPrice.objects.get(destination=booking.package)
        x=booking.no_of_People
        z=y.cost
        z=z*x
        ctx={'booking':booking,'cost':z}
        return render(request,'national/confirm_booking.html',ctx)

    def post(self,request,pk):
        booking=NBooking.objects.get(id=pk)
        booking.status='Confirmed'
        booking.save()
        return redirect('home:all')


