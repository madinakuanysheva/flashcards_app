from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):
    username = request.session.get('username')
    return render(request, 'users/layout.html', {'username': username})

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь уже существует')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('login')  # ОСТАВЛЯЕМ так
    return render(request, 'users/reg.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            request.session['username'] = username
            return redirect('index')
        else:
            messages.error(request, 'Неверный логин или пароль')
    return render(request, 'users/log.html')

def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('login')

