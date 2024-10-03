from django.shortcuts import render


def home_view(request):
    return render(request, 'index.html')


def login_view(request):
    pass


def register_view(request):
    pass
