from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Login and Logout URLs
    path('login/', LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # Optional: Register view if you want to handle user registration
    path('register/', views.register_view, name='register'),
]
