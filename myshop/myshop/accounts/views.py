from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('accounts:login_view')  # Перенаправьте на страницу профиля или другую страницу
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:registration')  # Перенаправьте на страницу профиля или другую страницу
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:login_view')  # Перенаправьте на страницу логина или другую страницу
