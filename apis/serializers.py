from rest_framework import serializers
from .models import Ganre, Author, Books, Order

class GanreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ganre
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"
