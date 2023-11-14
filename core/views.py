from django.shortcuts import render
from django.views.generic import ListView, DetailView
from items.models import Item

from django.core import paginator


def home(request):
    return render(request, 'core/home.html')


class ShopListView(ListView):
    model = Item
    template_name = 'core/shop.html'
    context_object_name = 'items'
    paginate_by = 2;


class ProductDetailView(DetailView):
    model = Item
    template_name = 'core/product_detail.html'
    context_object_name = 'product'
