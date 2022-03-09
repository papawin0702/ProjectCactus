from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters,generics
from rest_framework.viewsets import ModelViewSet
from store.models import Store

from store.models import Store
from store.serializer import StoreSerializer

class StoreView(ModelViewSet):
    queryset = Store.objects.order_by('pk')
    serializer_class = StoreSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    search_fields = ["name",]

    def update(self, request, *agrs, **kwargs):
        kwargs['partial'] = True
        return super().update(request,*agrs,**kwargs)
