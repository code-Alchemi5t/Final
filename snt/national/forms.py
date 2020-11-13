from django import forms
from national.models import NBooking

class CreateForm(forms.ModelForm):
    class Meta:
        model = NBooking
        fields = ['name','package','date','no_of_People','preferred_mode_of_travel','any_special_requests']
        widgets = {'date': forms.DateInput(attrs={'class':'datepicker'})}