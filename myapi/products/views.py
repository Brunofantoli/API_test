from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def product_list(request):
    products = [
        {'id': 1, 'name': 'Laptop', 'price': 1000},
        {'id': 2, 'name': 'Phone', 'price': 500},
    ]
    return JsonResponse({'products': products})