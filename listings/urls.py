# listings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('category/<int:category_id>/', views.item_list, name='item_list_by_category'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('item/new/', views.new_item, name='new_item'),
    path('item/<int:item_id>/edit/', views.edit_item, name='edit_item'),
    path('item/<int:item_id>/delete/', views.delete_item, name='delete_item'),
    path('item/<int:item_id>/mark_sold/', views.mark_sold, name='mark_sold'),
    path('my_items/', views.my_items, name='my_items'),
    path('search/', views.search_items, name='search_items'),
    path('favorite/<int:item_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('my_favorites/', views.my_favorites, name='my_favorites'),
    path('my_purchases/', views.my_purchases, name='my_purchases'),
    path('item/<int:item_id>/order/', views.order_item, name='order_item'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('sold_orders/', views.sold_orders, name='sold_orders'),
    path('order/<int:order_id>/complete/', views.complete_order, name='complete_order'),
]