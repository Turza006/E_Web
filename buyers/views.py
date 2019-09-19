from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Buyer

def bsignup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                buyer = Buyer.objects.get(name=request.POST['name'])
                return render(request,'buyers/signup.html', {'error':'Username has already been taken'})
            except Buyer.DoesNotExist:
                buyer = Buyer()
                buyer.name = request.POST['name']
                buyer.password = request.POST['password2']
                buyer.email = request.POST['email']
                buyer.save()
                return redirect('home')
        else:
            return render(request, 'buyers/signup.html', {'error':'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'buyers/signup.html')


def blogin(request):
    if request.method == 'POST':
        buyer = Buyer.objects.get(username=request.POST['username'],password=request.POST['password'])
        if buyer is not None:
            auth.login(request, buyer)
            return redirect('home')
        else:
            return render(request, 'buyers/login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'buyers/login.html')


def blogout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
