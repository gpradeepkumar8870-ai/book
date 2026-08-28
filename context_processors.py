from .models import Cart


def cart_summary(request):
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        return {'nav_cart_count': cart.total_items}
    return {'nav_cart_count': 0}
