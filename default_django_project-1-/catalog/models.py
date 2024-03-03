from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext as _


class User(AbstractBaseUser):  # noqa
    pass


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    exp_date = models.DateField()
    title = models.CharField(max_length=200)
    vendore_code = models.CharField(max_length=200)  # noqa


class City(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=200)


class Supplier(models.Model):
    city = models.OneToOneField(City, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)
    title = models.CharField(max_length=200)


class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    city = models.ForeignKey("City", on_delete=models.SET_NULL, null=True)
    email = models.EmailField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    product = models.ManyToManyField(Product, verbose_name=_("product"), help_text=_("Select a genre for this book"))


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
