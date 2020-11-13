# Create your models here.
from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.conf import settings

class NPackage(models.Model):
    destination = models.CharField(max_length=300)

    def __str__(self):
        return self.destination

class NConveyance(models.Model):
    conveyance=models.CharField(max_length=300)
    def __str__(self):
        return self.conveyance


class NBooking(models.Model):
    name = models.CharField(max_length=200, validators=[MinLengthValidator(2,"Name must be greater than 1 character")])
    package = models.ForeignKey('NPackage',on_delete=models.CASCADE, null=False)
    date = models.DateField()
    no_of_People=models.IntegerField(validators=[MinValueValidator(1,"Atleast one person should be on the trip!Or are you a Ghost?"), MaxValueValidator(30,"Bro a bus can only fit 30 people")])
    preferred_mode_of_travel=models.ForeignKey('NConveyance',on_delete=models.CASCADE)
    any_special_requests=models.TextField(null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=200,default='Not Confirmed')
    def __str__(self):
        return self.name

class NPrice(models.Model):
    cost=models.IntegerField(null=False)
    destination=models.ForeignKey('NPackage',on_delete=models.CASCADE,null=False)
    def __str__(self):
        return str(self.cost)
