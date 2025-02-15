from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('auth/login/', views.login_view, name='login'),
    path('auth/register/', views.register_view, name='register'),
    path('auth/logout/', views.logout_view, name='logout'),
    path('verify-email/<uidb64>/<token>/', views.logout_view, name='verify-email'),
]
