from django.db import models

class Ganre(models.Model):
    ganre_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.ganre_name

class Author(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.f_name
    
class Books(models.Model):
    name_book = models.CharField(max_length=50)
    page=models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)    
    ganre = models.ForeignKey(Ganre, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    descriptions = models.TextField()
    date_out = models.DateField(auto_now=False, auto_now_add=False) 
    created_at=models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name_book


class Order(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    count = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=1)
    created_at=models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.total_price = self.count * self.book.price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
    
    