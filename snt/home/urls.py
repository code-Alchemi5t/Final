from django.urls import path
from . import views
from django.views.generic import TemplateView
app_name='home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='all'),
    path('booking/', TemplateView.as_view(template_name='home/booking.html'), name='booking')
    # path("register",views.register,name="register"),
]
