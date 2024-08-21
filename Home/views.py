from django.db.models import Q
from django.shortcuts import render, redirect

from .models import Admin, Contact


def home(request):
    return render(request,'Home/home.html')

def about(request):
    return render(request,'Home/about.html')

def contactus(request):
    return render(request,'Home/contactus.html')

def login(request):
    return render(request,'Home/login.html')

def Register(request):
    return render(request,'Home/Register.html')
def forgotpassword(request):
    return render(request, 'Home/forgotpassword.html')

def base2(request):
    return render(request,'Home/base2.html')

def base(request):
    return render(request,'Home/base.html')

def checklogin(request):
    name = request.POST["username"]
    password = request.POST["pwd"]
    flag = Admin.objects.filter(Q(username=name) & Q(password=password))
    print(flag)

    if flag:
        return redirect('Home-base2')
    else:
        return redirect('Home-login')

def addregister(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['pwd']
        new_id =Admin(username=name, password=password)
        new_id.save()
        return redirect('Home-base')
def contactsave(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message=request.POST['message']
        new_id = Contact(name=name,email=email,message=message)
        new_id.save()
        return redirect('Home-base2')
