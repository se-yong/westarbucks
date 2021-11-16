from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

class Menu(models.Model):
    name = models.CharField(max_length=20)
    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    class Meta:
        db_table = 'categories'


class Allergy(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'allergy'

class Drink(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=CASCADE)
    korean_name = models.CharField(max_length=20)
    english_name = models.CharField(max_length=20)
    description = models.TextField()
    class Meta:    
        db_table = 'drink'

class Image(models.Model):
    image_url = models.CharField(max_length=200)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    class Meta:
        db_table = 'image'

class Allergy_drink(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

class Nutrition(models.Model):
    one_serving_kca = models.DecimalField(max_digits=10, decimal_places=2)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=2)
    saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=2)
    sugars_g = models.DecimalField(max_digits=10, decimal_places=2)
    protein_g = models.DecimalField(max_digits=10, decimal_places=2)
    caffeine_mg = models.DecimalField(max_digits=10, decimal_places=2)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    size = models.ForeignKey('Size', on_delete=models.CASCADE,)

class Size(models.Model):
    name = models.CharField(max_length=20)
    size_ml = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)