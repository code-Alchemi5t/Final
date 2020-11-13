from django import forms
from international.models import IBooking

class CreateForm(forms.ModelForm):
    class Meta:
        model = IBooking
        fields = ['name','package','date','no_of_People','preferred_mode_of_travel','any_special_requests']
        widgets = {'date': forms.DateInput(attrs={'class':'datepicker'})}