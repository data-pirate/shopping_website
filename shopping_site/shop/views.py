from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def product(request):
    return render(request, 'product.html')

def categories(request):
    return render(request, 'categories.html')