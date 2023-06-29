from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Category, Item


def category_page(request, category_id):
    category = get_object_or_404(Category, Q(pk=category_id) | Q(name__iexact=category_id))
    products = category.items.all()  # Access related items using 'items' attribute
    context = {'category': category, 'products': products}
    return render(request, 'category.html', context)
# Create your views here.

def index(request):
    return render(request, 'index.html')

from django.shortcuts import render
from .models import Category

def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})

def test(request):
    item = Item.objects.first()
    return render(request, 'test.html', {'item': item})

def add_to_cart(request, product_id):
    product = Item.objects.get(id=product_id)
    cart = request.session.get('cart', {})
    cart[product_id] = {
        'name': product.name,
        'price': product.price,
        'photo': product.photo.url,
    }
    request.session['cart'] = cart
    return redirect('cart')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if product_id in cart:
        del cart[product_id]
        request.session['cart'] = cart
    return redirect('cart')

def cart(request):
    cart = request.session.get('cart', {})
    return render(request, 'cart.html', {'cart': cart})


def success(request):
    return render(request, 'Success.html')








