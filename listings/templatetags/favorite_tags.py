from django import template
from listings.models import Favorite

register = template.Library()
 
@register.filter
def is_favorited(item, user):
    if not user.is_authenticated:
        return False
    return Favorite.objects.filter(user=user, item=item).exists() 