from django.db       import models
from django.db.models.deletion import SET_NULL

from users.models    import User
from products.models import Product

class Order(models.Model):
    order_status_id   = models.ForeignKey('OrderStatus', null=True, on_delete=models.SET_NULL)
    final_price       = models.DecimalField(max_digits=13, decimal_places=3)
    user_id           = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders'

class OrderStatus(models.Model):
    status = models.CharField(max_length=50)

    class Meta:
        db_table = 'order_status'

class OrderItem(models.Model):
    order_id   = models.ForeignKey('Order', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity   = models.IntegerField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'order_items'
    
class Payment(models.Model):
    order_id     = models.ForeignKey('Order', on_delete=models.CASCADE)
    method_id    = models.ForeignKey('Method', null=True, on_delete=SET_NULL)
    created_at   = models.DateTimeField(auto_now_add=True)
    final_amount = models.DecimalField(max_digits=13, decimal_places=3, null=True)
    status       = models.CharField(max_length=50, default='ready')
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'payments'

class Method(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'methods'
