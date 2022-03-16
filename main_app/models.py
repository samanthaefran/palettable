# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    brand = models.CharField(max_length=150)
    product_name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=65535, decimal_places=65535)
    website_link = models.CharField(max_length=150)
    tags = models.CharField(max_length=150)
    image_link = models.CharField(max_length=1000)
    product_description = models.CharField(max_length=4000)
    product_type = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'product'

    def __str__(self):
        return f'{self.product_name} by {self.brand}'

class Color(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    hex_value = models.CharField(max_length=7, blank=True, null=True)
    colour_name = models.CharField(max_length=150, blank=True, null=True)
    color_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'color'

    def __str__(self):
        return f'{self.hex_value} {self.colour_name}'


