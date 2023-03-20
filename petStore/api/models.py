from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Status(models.Model):
    title =  models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return self.title

class OrderStatus(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'OrderStatus'
        verbose_name_plural = 'OrderStatuses'

    def __str__(self):
        return self.title


class Type(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'

    def __str__(self):
        return self.title

class Pet(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    photo = models.ImageField(upload_to='images/')
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'

    def __str__(self):
        return self.name

class Order(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.PROTECT)
    count = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    date = models.DateField(auto_now=True)
    status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT)
    done = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return str(self.pet)