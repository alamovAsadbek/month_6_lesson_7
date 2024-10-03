from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from config.settings import EMAIL_HOST_USER
from pages.form import RegisterForm
from pages.token import email_token_generator


def send_email_verification(request, user):
    token = email_token_generator.make_token(request.user)
    uid = urlsafe_base64_encode(force_bytes(request.user.pk))
    domain = request.get_host()
    verification_url = reverse('verify-email', kwargs={'uidb64': uid, 'token': token})
    full_url = f'https://{domain}{verification_url}'

    text_content = render_to_string(
        'components/verify_email/verify_email.html',
        {'user': user, 'full_url': full_url}
    )

    message = EmailMultiAlternatives(
        subject='Verify your email',
        body=text_content,
        from_email=EMAIL_HOST_USER,
        to=[user.email]
    )

    message.attach_alternative(text_content, "text/html")
    message.send()


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
            send_email_verification(request, user)
            return redirect(reverse_lazy('login'))
        else:
            errors = form.errors
            return render(request, 'user-register.html', {'errors': errors})
    else:
        return render(request, 'user-register.html')


def logout_view(request):
    return redirect(reverse_lazy('login'))
