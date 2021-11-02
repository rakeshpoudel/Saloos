from django.urls import path
from .views import create,dashboard
urlpatterns= [
    path('create/',create,name='customer_create'),
    path('dashboard/',dashboard, name='cusdashboard')

]