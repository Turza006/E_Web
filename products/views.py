from django.shortcuts import render,redirect,get_object_or_404
from rest_framework import viewsets, permissions
from .models import Catagory, Products
from .serializers import CatagorySerializer, ProductsSerializer
from django.contrib.auth.decorators import login_required
from django.utils import timezone



def home(request):

    products = Products.objects

    return render(request, 'products/home.html',{'products':products})
def bhome(request):

    products = Products.objects

    return render(request, 'products/bhome.html',{'products':products})

class CatagoryView(viewsets.ModelViewSet):
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializer

class ProductsView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

@login_required(login_url="/sellers/signup")
def create(request):
    catagorys = Catagory.objects
    if request.method == 'POST':
        if request.POST['name'] and request.POST['detail'] and request.POST['catagorys'] and request.FILES['image'] and request.POST['price']:
            product = Products()
            cat = Catagory.objects
            product.name = request.POST['name']
            product.detail = request.POST['detail']
            product.catagorys = request.POST['catagorys']
            product.price = request.POST['price']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.seller = request.user
            product.save()
            return render(request, 'products/create.html',{'error':'Products Added'},{'catagorys':cat})
        else:
            return render(request, 'products/create.html',{'error':'All field are required'},{'catagorys':catagorys})
    else:
        return render(request, 'products/create.html',{'catagorys':catagorys})

def detail(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    return render(request, 'products/detail.html',{'products':product})


