from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import CustomUser, ChatRoom


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        profile_pic = request.FILES.get('profile_pic')

        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

        user = CustomUser(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            profile_pic=profile_pic,
            username=username
        )
        user.set_password(password)
        user.save()

        login(request, user)
        return redirect('index')

    return render(request, 'register.html')


def loginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('index')

        return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def logoutView(request):
    logout(request)
    return redirect('login')


@login_required
def indexView(request) :

    query  =  request.GET.get('q')

    if query :
        users  = CustomUser.objects.filter(Q(first_name__iconatins  =  query)
                                  |Q(email__icontains = query) |
                                  Q(last_name__icontains = query))
        return  render(request ,  {"data" , users})

    chatroom  = ChatRoom.objects.filter(participants = request.user)

    return render(request ,  'index.html' , {'data' : chatroom})