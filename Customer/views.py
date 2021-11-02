from django.shortcuts import render,redirect
from .forms import CustomerCreateform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def create(request):
    form = CustomerCreateform(request.POST or None)
    if form.is_valid():
        data = form.save(commit=False)
        data.user = request.user
        data.save()
        messages.add_message(request,messages.SUCCESS,"successfully customer created")
        return redirect('cusdashboard')

    return render(request,'customer/create.html',{'form':form})
@login_required(login_url='signin')
def dashboard(request):
    return render(request,'customer/dashboard.html')
