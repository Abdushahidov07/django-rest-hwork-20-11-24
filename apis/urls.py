from django.urls import path
from .views import *

urlpatterns = [
    path('genres/', GanreListAPIView.as_view(), name='genre-list'),
    path('genres/create/', GanreCreateAPIView.as_view(), name='genre-create'),
    path('genres/<int:pk>/', GanreRetrieveUpdateAPIView.as_view(), name='genre-detail'),
    path('genres/<int:pk>/delete/', GanreDestroyAPIView.as_view(), name='genre-delete'),

    path('authors/', AuthorListAPIView.as_view(), name='author-list'),
    path('authors/create/', AuthorCreateAPIView.as_view(), name='author-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateAPIView.as_view(), name='author-detail'),
    path('authors/<int:pk>/delete/', AuthorDestroyAPIView.as_view(), name='author-delete'),

    path('books/', BooksListAPIView.as_view(), name='book-list'),
    path('books/create/', BooksCreateAPIView.as_view(), name='book-create'),
    path('books/<int:pk>/', BooksRetrieveUpdateAPIView.as_view(), name='book-detail'),
    path('books/<int:pk>/delete/', BooksDestroyAPIView.as_view(), name='book-delete'),

    path('orders/', OrderListAPIView.as_view(), name='order-list'),
    path('orders/create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateAPIView.as_view(), name='order-detail'),
    path('orders/<int:pk>/delete/', OrderDestroyAPIView.as_view(), name='order-delete'),
]
