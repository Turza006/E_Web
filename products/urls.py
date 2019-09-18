from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('catagoryrest',views.CatagoryView)
router.register('productsrest',views.ProductsView)

urlpatterns = [
    path('', include(router.urls)),
    path('create',views.create,name = 'create'),
]

