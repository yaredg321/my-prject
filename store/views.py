from django.http.response import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import uploadform
from django.template.context import RequestContext
from .models import *


# Create your views here.
def up_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return render(request, 'up_login.html')
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return render(request, 'up_login.html')
	else:
		return render(request, 'up_login.html', {})

def register(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email =  request.POST['email']

        if password1==password2:

            if User.objects.filter(username=username).exists():
                messages.info(request,'username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
        else:
            messages.info(request,'password not maching..')        
        return redirect('/')

    else:
        return render(request, 'register.html')


# Create your views here.
def store(request):
    Products = Product.objects.all()
    context = {'products': Products}
    return render(request, 'store.html',context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = OrderItem.objects.filter(order=order)
        
    else:
        items = []
        order ={"get_cart_total":0, "get_cart_items": 0}
    context = {'items': items, 'order': order}
    return render(request, 'cart.html',  context)
    

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = OrderItem.objects.filter(order=order)
        
    else:
        items = []
        order ={"get_cart_total":0, "get_cart_items": 0}
    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context)

def detail(request, id=None):
    product = Product.objects.get(id=id)
    return render(request,  'detail.html', {"product": product})

def add_to_cart(request, id=None):
    if request.user.is_authenticated:
        product = Product.objects.get(id=id)
        customer = request.user.customer
        order, _ = Order.objects.get_or_create(customer=customer)
        OrderItem.objects.create(order=order, product=product)
        # return HttpResponse('created')
        return HttpResponseRedirect('/store/')

def upload(request):
    if request.method == 'POST':
           form = uploadform(request.POST, request.FILES)
           if form.is_valid():
               form.save()
           return HttpResponseRedirect('/upload/')
    else:
        return render(request, 'upload.html')