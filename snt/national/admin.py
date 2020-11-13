from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from national.models import NBooking, NConveyance, NPackage, NPrice

admin.site.register(NBooking)
admin.site.register(NConveyance)
admin.site.register(NPackage)
admin.site.register(NPrice)