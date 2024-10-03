from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from pages.form import RegisterForm
from pages.token import email_token_generator


def send_email_verification(request):
    token = email_token_generator.make_token(request.user)
    uid = urlsafe_base64_encode(force_bytes(request.user.pk))
    domain = request.get_host()
    full_url = f"http://{domain}/verify-email/{uid}/{token}"


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
            return redirect(reverse_lazy('login'))
        else:
            errors = form.errors
            return render(request, 'user-register.html', {'errors': errors})
    else:
        return render(request, 'user-register.html')


def logout_view(request):
    pass
