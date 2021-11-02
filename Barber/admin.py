from django.contrib import admin
from .models import Barber,Service,Request

# Register your models here.
admin.site.register([Barber,Service,Request])

