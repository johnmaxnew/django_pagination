from django.db import models



class Product(models.Model):
    
    CONDITION_TYPE = (
        ("New", "New"),
        ("Used", "Used")
    )
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length= 500)
    price = models.DecimalField(max_digits= 10, decimal_places=2)
    brand = models.ForeignKey('Brand', on_delete= models.SET_NULL, null = True)
    condition = models.CharField(max_length = 100, choices = CONDITION_TYPE)
    created = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to = 'main_product/', blank = True, null = True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    brand_name = models.CharField(max_length = 50)

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'



    def __str__(self):
        return self.brand_name