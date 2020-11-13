# Register your models here.
from django.contrib import admin

# Register your models here.
from international.models import IBooking, IConveyance, IPackage, IPrice

admin.site.register(IBooking)
admin.site.register(IConveyance)
admin.site.register(IPackage)
admin.site.register(IPrice)