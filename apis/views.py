from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import *
from .serializers import *


class GanreListAPIView(ListAPIView):
    queryset = Ganre.objects.all()
    serializer_class = GanreSerializer 
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['ganre_name',] 
    search_fields = ['ganre_name',]

class GanreCreateAPIView(CreateAPIView):
    queryset = Ganre.objects.all()
    serializer_class = GanreSerializer

class GanreRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Ganre.objects.all()
    serializer_class = GanreSerializer


class GanreDestroyAPIView(DestroyAPIView):
    queryset = Ganre.objects.all()


class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer 
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['f_name','l_name',] 
    search_fields = ['f_name',]
    
class AuthorCreateAPIView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDestroyAPIView(DestroyAPIView):
    queryset = Author.objects.all()

class BooksListAPIView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer 
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['name_book','author','ganre',"date_out"] 
    ordering_fields = ['price', 'page'] 
    search_fields = ['name_book',]

class BooksRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksDestroyAPIView(DestroyAPIView):
    queryset = Books.objects.all()    

class BooksCreateAPIView(CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer



class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer 
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    filterset_fields = ['book','username',] 
    ordering_fields = ['created_at', 'total_price',"count"] 
    search_fields = ['username',]

class OrderRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDestroyAPIView(DestroyAPIView):
    queryset = Order.objects.all()    

class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer