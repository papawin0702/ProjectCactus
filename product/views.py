from audioop import reverse
from itertools import product
from multiprocessing.reduction import duplicate
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters,generics
from rest_framework.viewsets import ModelViewSet

from product.models import Category, Product
from product.serializer import CategorySerializer, ProductSerializer

# Create your views here.

class CategoryView(ModelViewSet):
    queryset = Category.objects.order_by('pk')
    serializer_class = CategorySerializer

class ProductView(ModelViewSet):
    queryset = Product.objects.order_by('pk')
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    search_fields = ["name","category__name","category__category__name"]
    filterset_fields = ["category","category__category"]

    def update(self, request, *agrs, **kwargs):
        kwargs['partial'] = True
        return super().update(request,*agrs,**kwargs)

def cart_add(request, ca):
    product = get_object_or_404(Product, ca=ca)
    cart_items = request.session.get['cart_items'] or []

    duplicated = False
    for c in cart_items:
        if c.get('ca') == product.ca:
            c['qty'] = int(c.get('qty') or '1') + 1
            duplicated = True
    if not duplicated:
        cart_items.append({
            'name':product.name,
            'price':product.price
        })
    return HttpResponseRedirect(reverse('product:cart_list', kwargs={}))

def cart_list(requset):
    cart_items = requset.session.get('cart_items') or []

    total_qty = 0
    for c in cart_items:
        total_qty = total_qty + c.get('qty')

    requset.session['cart_qty'] = total_qty
    return redirect(requset, 'cart.html',{
        'cart_items': cart_items,
    })