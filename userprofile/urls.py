from django.urls import path
from . import views

urlpatterns = [
    path("",views.userinfo,name="userinfo"),
    path('user_info/', views.user_info_view, name='user_info_form'),
    path('login/',views.login_request,name='login_request'),
    path('register/',views.register_request,name="register_request")


]

