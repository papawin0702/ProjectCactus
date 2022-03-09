from audioop import reverse
from cmath import log
import imp
from itertools import product
import re
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from account.forms import MyUserCreationForm as UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from product.models import Product,Category
from store.models import Store

def home(request):
    return render(request,'home.html')

def shopall(request):
    return render(request,'cactus.html')

def story(request):
    return render(request,'story.html')

def about(request):
    return render(request,'about.html')

def help(request):
    return render(request,'help.html')

def log(request):
    return render(request,'login.html')

def cart_view(request):
    return render(request,'cart.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')          
    else:
        messages.success(request, ("ล็อกอินไม่สำเร็จ โปรดลองอีกครั้ง..."))
        form = AuthenticationForm()
    return render(request, 'login.html', {
        'form': form
        })

def logout_view(request):
    logout(request)
    return redirect('/')



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            login (request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def displayproduct(request):
    data = Product.objects.all()
    context = {
        'Products' : data
    }
    return render(request, 'cactus.html', context)

def displaystore(request):
    data = Store.objects.all()
    context = {
        'Stores' : data
    }
    return render(request, 'home.html', context)
