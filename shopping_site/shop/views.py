from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'product': products})

def search(request):
    try:
        q = request.GET['q']
    except:
        q = None
    
    if q:
        products = Product.objects.filter(product_name__icontains=q)
        results = {'query': q, 'products': products}
        return render(request, 'results.html', results)
    else:
        results = {}
        return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def product(request, id, name):
    product = Product.objects.get(id=id)
    return render(request, 'product.html', {'product': product})

def categories(request):
    return render(request, 'categories.html')

def signup(request):
    return render(request, 'signup.html')

def handle_signup(request):
    if request.method == 'POST':
        fullname = request.POST['reg_fullname']
        username = request.POST['reg_username']
        email = request.POST['reg_email']
        password = request.POST['reg_password']
        confirm_password = request.POST['reg_password_confirm']
        gender = request.POST['reg_gender']
        if password == confirm_password:
            try:
                user = User.objects.get(username=username)
                return render(request, 'signup.html', {'error': True, 'message': 'Username already exists'})
            except:
                user = User.objects.create_user(username=username, password=password)
                return redirect('login')
        else:
            return render(request, 'signup.html', {'error': True, 'message': 'Passwords don\'t match'})    
    else:
        return render(request, 'signup.html', {'error': True, 'message': 'Something went Wrong ! please try again'})    

def login(request):
    return render(request, 'login.html')
def handle_login(request):
    if request.method == 'POST':
        username = request.POST['lg_username']
        password = request.POST['lg_password']
        remember = request.POST['lg_remember']
        if not remember:
            remember = 'off'
        user = auth.authenticate(username=username, password=password)
        if not user is None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': True, 'message': 'Invalid  Credentials'})
def forgot_password(request):
    return render(request, 'forgot_password.html')