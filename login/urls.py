from django.urls import path
from django.contrib.auth import views as auth_views

from login import views

urlpatterns = [
    path('login', auth_views.LoginView.as_view(
        template_name="login/form.html"
    ), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

    path('register', views.register, name='register'),
]
