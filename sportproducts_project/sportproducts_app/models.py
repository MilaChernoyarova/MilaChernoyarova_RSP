from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=500)
    price = models.IntegerField()
    discription = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=1000)
    model = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.title} {self.model}"
    

class MyProduct(models.Model):
    title = models.CharField(max_length=500)
    price = models.IntegerField()
    discription = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=1000)
    model = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.title} {self.model}"
    