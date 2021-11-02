from django.urls import path,include
from .views import signup,signin,dashboard,who,signout



urlpatterns = [
    path('signup',signup,name='signup'),
    path('signin',signin,name='signin'),
    path('signout',signout,name='signout'),
    path('dashboard',dashboard,name='dashboard'),
    path('who',who,name='who'),
    path('customer',include('Customer.urls')),
    path('barber',include('Barber.urls')),



]