from django.db import models

# Create your models here.
class product(models.Model):
    product_id= models.AutoField
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    productdate= models.DateField()
    productImage = models.ImageField(upload_to="shop/media",default="")