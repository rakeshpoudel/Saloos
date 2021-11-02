from django.shortcuts import render,redirect
from .forms import BarberCreateform
from .models import Barber,Service
from .forms import AddServiceForm,ChangeProfileImageform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def create(request):
    form = BarberCreateform(request.POST or None)
    if form.is_valid():
        data = form.save(commit=False)
        data.user = request.user
        data.save()
        messages.add_message(request,messages.SUCCESS,"successfully customer created")
        return redirect('bardashboard')

    return render(request,'barber/create.html',{'form':form})
@login_required(login_url='signin')
def dashboard(request):
    e = getCurrentlyLoginBarber(request.user)
    serviceForm = AddServiceForm(request.POST or None, request.FILES or None)
    changeImageForm = ChangeProfileImageform(request.POST or None,
                                             request.FILES or None,instance=e)
    if changeImageForm.is_valid():
        changeImageForm.save()
        messages.add_message(request,messages.SUCCESS,"sucessfully changed")
    context = {}
    context.update({'changeImageForm':changeImageForm})
    if serviceForm.is_valid():
        data = serviceForm.save(commit=False)
        data.barber = e
        data.save()
        messages.add_message(request,messages.SUCCESS,"sucessfully saved")
        serviceForm = AddServiceForm()
    context.update({'serviceform':serviceForm})
    services = Service.objects.filter(barber=e)
    context.update({'services':services})
    if e == None:
        return redirect('logout')
    else:
        context.update({'barber':e})
    return render(request,'barber/dashboard.html',context)

def getCurrentlyLoginBarber(user):
    try:
        return Barber.objects.get(user=user)
    except:
        return None

def delete(request,id):
    data = Service.objects.get(id=id)
    data.delete()
    return redirect('bardashboard')

def Aboutme(request):
    return render(request,'aboutme.html',)