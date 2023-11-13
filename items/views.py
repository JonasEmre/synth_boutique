from django.shortcuts import render

def detail(request, item_id):
    return render(request, 'items/details.html')
