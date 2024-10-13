from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="dashboard"),
    path("scheduler", views.scheduler, name="scheduler")
]

