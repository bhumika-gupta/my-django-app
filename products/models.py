from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=225)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


# steps for migration:

# create a model with these attributes,

# 2 terminal commands: one to create a new migration based on changes in our code
# and another to make appending migrations

# create a model class that offers discounts
# in the class, 3 attributes: code (textual field), description (max char of 250 maybe), discount (floating thing)
# create migrations

class Offer(models.Model):
    code = models.CharField(max_length=15)
    description = models.CharField(max_length=250)
    discount = models.FloatField(max_length=50)

# terminal commands:
# making migrations: python3 manage.py makemigrations
# appending migrations: python3 manage.py migrate

# REMEMBER TO DRAG AND DROP AFTER MIGRATIONS







