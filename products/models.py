from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length= 500)
    price = models.DecimalField(max_digits= 10, decimal_places=2)
    published = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to = 'main_product/', blank = True, null = True)

    def __str__(self):
        return self.name
