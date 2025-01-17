from django.db import models
from users.models import Accounts,Carts
from shop.models import Products
from payments.models import Payments
# Create your models here.

class Orders(models.Model):
    ''' fetching order made by users '''
    order_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    customer_id = models.ForeignKey(Accounts,on_delete=models.CASCADE)
    order_amount = models.DecimalField(max_digits=10,decimal_places=2)
    order_date = models.DateTimeField(auto_now=True)
    shipping_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    status = models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)

    def __int__(self):
        return self.order_id
    
    
class OrderDetails(models.Model):
    order_id = models.ForeignKey(Orders,on_delete=models.CASCADE)
    products_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    payment_id = models.ForeignKey(Payments,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    payment_status = models.CharField(max_length=20)
    cart_id = models.ForeignKey(Carts,on_delete=models.PROTECT)


    def __int__(self):
        return self.order_id
    
    