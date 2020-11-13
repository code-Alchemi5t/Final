# Create your views here.
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from international.owner import OwnerDeleteView, OwnerUpdateView
from django.urls import reverse
from international.forms import CreateForm
from international.models import IBooking, IPrice
from django.shortcuts import render, redirect


class NewBookingDeleteView(OwnerDeleteView):
    model = IBooking
    success_url='international:all'
    template_name = 'international/booking_confirm_delete.html'


class NewBookingCreate(LoginRequiredMixin, View):
    template_name='international/booking_form.html'
    success_url='international:all'
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
        return redirect(reverse('international:confirm_booking', args=[booking.id]))


class ConfirmBooking(LoginRequiredMixin, View):
    def get(self,request,pk):
        booking=IBooking.objects.get(id=pk)
        y=IPrice.objects.get(destination=booking.package)
        x=booking.no_of_People
        z=y.cost
        z=z*x
        ctx={'booking':booking,'cost':z}
        return render(request,'international/confirm_booking.html',ctx)

    def post(self,request,pk):
        booking=IBooking.objects.get(id=pk)
        booking.status='Confirmed'
        booking.save()
        return redirect('home:all')


