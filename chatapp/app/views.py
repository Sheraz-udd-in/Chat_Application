from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import ChatRoom, UserInfo, Message


@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')

    # Optional message for redirected users
    if 'next' in request.GET:
        messages.warning(request, 'You must log in to access this page.')

    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        image = request.FILES.get('image')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('register')

        user = User.objects.create_user(username=username, password=password)
        user_info = UserInfo.objects.create(
            user=user,
            name=name,
            email=email,
            phone=phone,
            image=image
        )
        login(request, user)
        messages.success(request, "Registration successful")
        return redirect('index')

    return render(request, 'register.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

