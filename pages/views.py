from django.shortcuts import render

from pages.form import RegisterForm


def home_view(request):
    return render(request, 'index.html')


def login_view(request):
    return render(request, 'user-login.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.save()
    return render(request, 'user-register.html')
