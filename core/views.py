from django.shortcuts import render
from items.models import Item


def home(request):
    return render(request, 'core/home.html')

def shop(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'core/shop.html', context=context)
