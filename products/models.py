from django.db import models

# Create your models here.
class Products(models.Model):
    id_product = models.IntegerField(primary_key=True)
    name_prod =models.CharField(max_length=50, blank=True, null=False)
    price_prod =models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=False)
    stock_prod =models.IntegerField(blank=True, null=False)

