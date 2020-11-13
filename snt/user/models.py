from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.
class UserProfile(models.Model):
    phone_number = models.CharField(blank=True, max_length=11, validators=[MinLengthValidator(9,"Enter a valid number"), MaxLengthValidator(11,"Enter a valid number")], null=True)
    address = models.TextField(blank=True)
    alternate_email = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

