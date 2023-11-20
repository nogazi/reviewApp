from django.shortcuts import render
from .forms import ContactForm
from .models import Product
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import ProductForm


def home_view(request):
    return render(request, 'base.html')

def about_us_view(request):
    return render(request, 'reviews/about_us.html')

def contact_us_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (you can add email sending logic here)
            return render(request, 'reviews/contact_us_success.html')  # Redirect to a success page
    else:
        form = ContactForm()

    return render(request, 'reviews/contact_us.html', {'form': form})

def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'reviews/product_list.html', {'products': products})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegistrationForm()

    return render(request, 'reviews/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')

    else:
        form = LoginForm()

    return render(request, 'reviews/login.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'reviews/profile.html')

@login_required
def add_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added a product')
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'reviews/add_product.html', {'form': form})