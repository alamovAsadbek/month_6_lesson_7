from django.shortcuts import render


def home_view(request):
    return render(request, 'index.html')


def login_view(request):
    return render(request, 'user-login.html')


def register_view(request):
    return render(request, 'user-register.html')
