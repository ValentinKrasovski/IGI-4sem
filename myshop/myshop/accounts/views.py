from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('shop:home')  # Перенаправьте на страницу профиля или другую страницу
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('shop:home')  # Перенаправьте на страницу профиля или другую страницу
    form = LoginForm()  # Создание пустой формы для отображения на странице
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'logout.html')  # Перенаправьте на страницу логина или другую страницу
