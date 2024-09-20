from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    available = models.BooleanField(default=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

class User(models.Model):
    email = models.EmailField(unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()

    def __str__(self):
        return f"{self.user} borrowed {self.book}"
