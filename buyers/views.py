from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def bsignup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'],first_name=(request.POST['type']))
                return render(request, 'buyers/signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=(request.POST['username']), password=(request.POST['password1']),email=(request.POST['email']),first_name=(request.POST['type']))
                auth.login(request,user)
                return redirect('bhome')
        else:
            return render(request, 'buyers/signup.html', {'error':'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'buyers/signup.html')

def blogin(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('bhome')
        else:
            return render(request, 'buyers/login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'buyers/login.html')

def blogout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
