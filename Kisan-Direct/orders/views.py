from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Order

@login_required
def my_orders(request):
    orders = request.user.orders.select_related('product', 'product__farmer')
    return render(request, 'orders.html', {'orders': orders, 'incoming': False})

@login_required
def incoming(request):
    orders = Order.objects.filter(product__farmer=request.user).select_related('product', 'buyer')
    return render(request, 'orders.html', {'orders': orders, 'incoming': True, 'statuses': Order.STATUS})

@login_required
def update_status(request, pk):
    order = get_object_or_404(Order, pk=pk, product__farmer=request.user)
    new = request.POST.get('status')
    if request.method == 'POST' and new in dict(Order.STATUS):
        if new == 'cancelled' and order.status != 'cancelled':
            order.product.quantity += order.quantity
            order.product.save()
        order.status = new
        order.save()
        messages.success(request, f'Order marked {new}.')
    return redirect('incoming_orders')
