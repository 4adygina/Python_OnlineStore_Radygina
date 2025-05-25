from django.contrib.auth.models import AbstractUser

from django.db import models

# Create your models here.
class User(AbstractUser):
  pass

class Clients(models.Model):
  client_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  adress = models.TextField(null=True)
  phone_number = models.CharField(max_length=12)
  email = models.EmailField(null=True ,max_length=255)

  def str(self):
    return [self.client_name]("http://self.client_name/")

class Basket(models.Model):
  client_id = models.ForeignKey('Clients', on_delete=models.PROTECT)
  basket_items_id = models.ForeignKey('Basket_items', on_delete=models.PROTECT)
  basket_price = models.DecimalField(max_digits=7, decimal_places=2)

  def str(self):
    return [self.basket_price]('http://self.basket_price/')

class Basket_items(models.Model):
  good_id = models.ForeignKey('Goods', on_delete=models.PROTECT)
  quantity_of_good_in_basket = models.IntegerField()
  image = models.ImageField(upload_to='basket_items/')

  def str(self):
    return [self.quantity_of_good_in_basket]("http://self.quantity_of_good_in_basket/")

class Goods(models.Model):
  good_name = models.CharField(max_length=255)
  good_price = models.DecimalField(max_digits=7, decimal_places=2)
  good_image = models.ImageField(upload_to='goods/')
  description = models.TextField(null=True)

  def str(self):
    return [self.good_name]("http://self.good_name/")

class Stock(models.Model):
  good_id = models.ForeignKey('Goods', on_delete=models.PROTECT)
  quantity_of_good = models.IntegerField()
  city = models.CharField(max_length=255)

  def str(self):
    return [self.quantity_of_good]("http://self.quantity_of_good/")

class Order_details(models.Model):
  good_id = models.ForeignKey('Goods', on_delete=models.PROTECT)
  order_id = models.ForeignKey('Orders', on_delete=models.PROTECT)
  stock_id = models.ForeignKey('Stock', on_delete=models.PROTECT)
  status = models.CharField(max_length=255)

class Orders(models.Model):
  client_id = models.ForeignKey('Clients', on_delete=models.PROTECT)
  basket_id = models.ForeignKey('Basket', on_delete=models.PROTECT)

class Stock_balance(models.Model):
  good = models.OneToOneField(Goods, verbose_name='Товар', on_delete=models.CASCADE)
  count = models.IntegerField(verbose_name='Количество')
  