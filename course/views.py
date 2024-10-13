from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "course/dashboard.html")

def scheduler(request):
    return render(request, "course/scheduler.html")