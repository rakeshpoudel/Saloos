from django.urls import path
from .views import create,dashboard,delete,Aboutme
urlpatterns= [
    path('create/',create,name='barber_create'),
    path('dashboard/',dashboard, name='bardashboard'),
    path('deleteservice/<int:id>',delete,name='delete_service'),
    path('aboutme/',Aboutme,name='aboutme'),

]