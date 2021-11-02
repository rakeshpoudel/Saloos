from django.shortcuts import render,redirect
from django.http import HttpResponse
from myUser.models import CustomUser
from django.contrib import messages
from django.core.exceptions import ValidationError
from .forms import LoginForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from Customer.models import Customer
from Barber.models import Barber

# Create your views here.
from .forms import SignUpForm
def signup(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        try:
            form.save()
            messages.add_message(request,messages.SUCCESS,"sucessfully account created")
            return redirect("signin")
        except ValidationError as e:
            messages.add_message(request,messages.ERROR,e.messages)

    return render(request,'signup.html',{'form':form})

    #  if request.method=='GET':
    #     context = {
    #         'form':SignUpForm()
    #     }
    #     return render(request,'signup.html',context)
    # else:
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponse("sign success")
    #     return HttpResponse("error occured")
    #     email = request.POST['email']
        # pass1 = request.POST['pass1']
        # pass2 = request.POST['pass2']
        # contact = request.POST['contact']
        # if pass1==pass2:
        #     c = CustomUser(email=email,contactNo=contact)
        #     c.set_password(pass1)
        #     c.save()
        #     return HttpResponse("user accont created sucessfully")
        # else:
        #     return HttpResponse("username and password doesnot match")
        #

def signin(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        e = request.POST['email']
        p = request.POST['password']
        user = authenticate(email=e,password=p)
        if user is not None:
            login(request,user)
            if not isCustomer(request.user.id) and not isBarber(request.user.id):
                return redirect('who')
            if isCustomer(request.user.id):
                return redirect('cusdashboard')
            if isBarber(request.user.id):
                return redirect('bardashboard')
        else:
            messages.add_message(request,messages.SUCCESS,"username and password does not valid")
    return render(request,'login.html',{'form':form})


@login_required(login_url='signin')
def dashboard(request):
    return HttpResponse("<h1>DashBoard</h1>")

@login_required(login_url='signin')
def who(request):
    return render(request,'who.html')


def isCustomer(user_id):
    try:
        e = Customer.objects.get(user_id=user_id)
        return True
    except:
        return False

def isBarber(user_id):
    try:
        e = Barber.objects.get(user_id=user_id)
        return True
    except:
        return False

def signout(request):
    logout(request)
    return redirect('signin')


