from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from orders.forms import OrderForm
from .forms import ProductForm
from .models import Product

def home(request):
    q, cat = request.GET.get('q', ''), request.GET.get('category', '')
    items = Product.objects.filter(is_available=True, quantity__gt=0).select_related('farmer')
    if q:
        items = items.filter(Q(name__icontains=q) | Q(farmer__village__icontains=q) | Q(farmer__district__icontains=q))
    if cat:
        items = items.filter(category=cat)
    return render(request, 'home.html', {'items': items, 'q': q, 'cat': cat, 'categories': Product.CATEGORIES})

def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = OrderForm(request.POST or None)
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        if request.user.role != 'buyer':
            messages.error(request, 'Only buyer accounts can place orders.')
        elif form.is_valid():
            order = form.save(commit=False)
            if order.quantity > product.quantity:
                form.add_error('quantity', f'Only {product.quantity} {product.unit} left.')
            else:
                order.buyer, order.product = request.user, product
                order.total = order.quantity * product.price
                order.save()
                product.quantity -= order.quantity
                product.save()
                messages.success(request, 'Order placed. The farmer will confirm it soon.')
                return redirect('my_orders')
    return render(request, 'detail.html', {'p': product, 'form': form})

@login_required
def add_product(request):
    if request.user.role != 'farmer':
        messages.error(request, 'Only farmer accounts can list produce.')
        return redirect('home')
    form = ProductForm(request.POST or None)
    if form.is_valid():
        product = form.save(commit=False)
        product.farmer = request.user
        product.save()
        messages.success(request, 'Produce listed.')
        return redirect('my_products')
    return render(request, 'form.html', {'form': form, 'title': 'List your produce', 'button': 'Publish listing'})

@login_required
def my_products(request):
    return render(request, 'my_products.html', {'items': request.user.products.all()})
