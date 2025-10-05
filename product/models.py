from django.db import models

# Create your models here.

class ProductList(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.TextField(max_length=50)
    category = models.TextField(max_length=20)
    price = models.FloatField()
    pimage = models.ImageField(upload_to='images/',null=True,blank=True)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.pname 