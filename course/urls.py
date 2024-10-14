from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/",views.dashboard ,name="dashboard"),
    path("scheduler", views.scheduler, name="scheduler")
]

