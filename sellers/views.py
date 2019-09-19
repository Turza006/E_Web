from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Seller

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                seller = Seller.objects.get(name=request.POST['name'])
                return render(request, 'sellers/signup.html', {'error': 'Username has already been taken'})
            except Seller.DoesNotExist:
                seller = Seller()
                seller.name = request.POST['name']
                seller.password = request.POST['password2']
                seller.email = request.POST['email']
                seller.save()
                return redirect('create')
        else:
            return render(request, 'sellers/signup.html', {'error':'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'sellers/signup.html')

def login(request):
    if request.method == 'POST':
        seller = Seller.objects.get(username=request.POST['username'], password=request.POST['password'])
        if seller is not None:
            auth.login(request, seller)
            return redirect('create')
        else:
            return render(request, 'sellers/login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'sellers/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')