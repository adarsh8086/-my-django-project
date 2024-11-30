from django.db import models
from django.contrib.auth.models import User

# Create your models here.






class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
   

    def __str__(self):
        return self.name


    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, choices=[('Paid', 'Paid'), ('Pending', 'Pending')], default='Pending')
    payment_method = models.CharField(max_length=50, choices=[('COD', 'Cash on Delivery'), ('GPay', 'Google Pay'), ('PhonePe', 'PhonePe'), ('Card', 'Card')])


    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
    


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order,null=True, blank=True, on_delete=models.CASCADE, related_name='purchases')  # Foreign key to Order and Allow nulls


    def __str__(self):
        return f'{self.user.username} - {self.product.name}'




class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=[('Paid', 'Paid'), ('Pending', 'Pending')], default='Pending')
    payment_method = models.CharField(max_length=50, choices=[('COD', 'Cash on Delivery'), ('GPay', 'Google Pay'), ('PhonePe', 'PhonePe'), ('Card', 'Card')])


    @property
    def subtotal(self):
        return self.quantity * self.price

    def __str__(self):
        return f"Order #{self.order.id} - {self.product.name} (Qty: {self.quantity})"



class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
    
