from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import Group
from clients.models import Product
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, User
from django.urls import reverse
from django.contrib import messages


def clients_main(request):
    return render(request,'clients/main.html')


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('dashboard'))  # перенаправление на главную страницу после входа
    else:
        form = AuthenticationForm()
    return render(request, 'clients/login2.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Замените 'home' на имя нужного URL для перенаправления
    else:
        form = UserCreationForm()

    return render(request, 'clients/register.html', {'form': form})


def list(request):
    products = Product.objects.all()
    return render(request, 'clients/list.html', {'products': products})

def stuff(request):
    users = User.objects.all()
    return render(request, 'clients/stuff.html', {'users': users})