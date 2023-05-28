from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *
import json

def produit_filter(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product/product.html', {'product': product})

def product(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        order = {
            'get_cart_items': 0,
            'get_cart_total': 0
        }
        cartItems = order['get_cart_items']

    context = {
        'products': products,
        'order': order,
        'cartItems': cartItems,
        'categories': categories,
    }

    return render(request, 'product/product.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        
    else:
        items = []
        order = {
            'get_cart_items': 0,
            'get_cart_total': 0
        }
        cartItems = order['get_cart_items']

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }

    return render(request, 'product/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        order = {
            'get_cart_items': 0,
            'get_cart_total': 0
        }

    context = {
        'order': order
    }

    return render(request, 'product/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

