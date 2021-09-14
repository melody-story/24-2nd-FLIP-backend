from django.db       import models

from products.models import Product
from users.models    import User

class Cart(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id    = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity   = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'carts'

