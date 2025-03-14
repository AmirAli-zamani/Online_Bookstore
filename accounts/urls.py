from django.urls import path
from .views import register_user
from django.contrib.auth.views import LoginView
from .profile import profile


urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', register_user, name='register'),
    path('profile/', profile, name='profile'),
]
