from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from catalog.models import Book
from .models import Cart, CartItem


@login_required
def cart_detail_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = cart.items.select_related('book').all()
    shipping_fee = 0
    if cart.subtotal > 0:
        from django.conf import settings as dj_settings
        shipping_fee = 0 if cart.subtotal >= dj_settings.FREE_SHIPPING_THRESHOLD else dj_settings.STANDARD_SHIPPING_FEE
    context = {
        'cart': cart,
        'items': items,
        'shipping_fee': shipping_fee,
        'grand_total': cart.subtotal + shipping_fee,
    }
    return render(request, 'cart/cart_detail.html', context)


@login_required
@require_POST
def cart_add_view(request, book_id):
    book = get_object_or_404(Book, id=book_id, is_active=True)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    quantity = int(request.POST.get('quantity', 1))

    if not book.in_stock:
        messages.error(request, f"Sorry, '{book.title}' is currently out of stock.")
        return redirect(request.META.get('HTTP_REFERER', 'catalog:home'))

    item, created = CartItem.objects.get_or_create(cart=cart, book=book, defaults={'quantity': quantity})
    if not created:
        item.quantity += quantity

    if item.quantity > book.stock_quantity:
        item.quantity = book.stock_quantity
        messages.warning(request, f"Only {book.stock_quantity} copies of '{book.title}' available. Cart updated to max available quantity.")
    item.save()
    messages.success(request, f"'{book.title}' added to your cart.")
    return redirect(request.META.get('HTTP_REFERER', 'cart:cart_detail'))


@login_required
@require_POST
def cart_update_view(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    if quantity <= 0:
        item.delete()
        messages.info(request, "Item removed from cart.")
    else:
        quantity = min(quantity, item.book.stock_quantity)
        item.quantity = quantity
        item.save()
        messages.success(request, "Cart updated.")
    return redirect('cart:cart_detail')


@login_required
def cart_remove_view(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    messages.info(request, "Item removed from cart.")
    return redirect('cart:cart_detail')


@login_required
def cart_clear_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart.items.all().delete()
    messages.info(request, "Cart cleared.")
    return redirect('cart:cart_detail')
