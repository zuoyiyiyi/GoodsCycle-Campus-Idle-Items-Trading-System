# listings/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "Categories"

class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='favorited_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'item')

    def __str__(self):
        return f'{self.user.username} 收藏了 {self.item.title}'

class Item(models.Model):
    STATUS_CHOICES = (
        ('available', '可购买'),
        ('reserved', '已预定'),
        ('sold', '已售出'),
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    condition = models.CharField(max_length=100)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='purchased_items')
    
    def __str__(self):
        return self.title

class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='items/')
    
    def __str__(self):
        return f"{self.item.title}的图片"

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', '待确认'),
        ('completed', '已完成'),
        ('cancelled', '已取消'),
    ]
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='orders')
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders_made')
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders_received')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"订单：{self.item.title} - 买家：{self.buyer.username}"