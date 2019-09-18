from django.shortcuts import render,redirect
from rest_framework import viewsets, permissions
from .models import Catagory, Products
from .serializers import CatagorySerializer, ProductsSerializer
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def home(request):
    products = Products.objects
    return render(request, 'products/home.html',{'products':products})

class CatagoryView(viewsets.ModelViewSet):
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializer

class ProductsView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['name'] and request.POST['details'] and request.POST['url'] and request.POST['catagorys'] and request.FILES['image']:
            product = Products()
            product.name = request.POST['name']
            product.details = request.POST['details']
            product.catagorys = request.POST['catagorys']
            if request.POST['url'].startwith('http://') or request.POST['url'].startwith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://'+ request.POST['url']
                product.image= request.FILES['image']
                product.pub_date=timezone.datetime.now()
                product.seller = request.user
                product.save()
                return redirect('home')
        else:
            return render(request, 'products/create.html',{'error':'All field are required'})
    else:
        return render(request, 'products/create.html')