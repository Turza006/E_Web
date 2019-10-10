from django.urls import path, include
from . import views
from .views import create
from rest_framework import routers

router = routers.DefaultRouter()
router.register('catagoryrest',views.CatagoryView)
router.register('productsrest',views.ProductsView)

urlpatterns = [
    path('', include(router.urls)),
    path('create/',create,name ='create'),
    path('bhome/', views.bhome, name='bhome'),
]

