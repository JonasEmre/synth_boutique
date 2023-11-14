from django.urls import path, include
from . import views
from .views import ShopListView, ProductDetailView

urlpatterns = [
    path('', views.home , name='home'),
    path('shop/', ShopListView.as_view() , name='shop'),
    path('shop/product_detail/<int:pk>/', ProductDetailView.as_view() , name='product-detail'),
]

