import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campus_glimmer.settings')
django.setup()

from listings.models import Order

count = 0
for order in Order.objects.filter(status='completed'):
    item = order.item
    if item.status != 'sold':
        item.status = 'sold'
        item.save()
        print(f'已将商品"{item.title}"状态改为已售出')
        count += 1
print(f'同步完成，共更新{count}个商品。') 