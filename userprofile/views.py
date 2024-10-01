from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import UserInfoForm

def userinfo(request):
    return HttpResponse("Hello World")

def user_info_view(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return HttpResponse('User information has been saved successfully!')
    else:
        form = UserInfoForm()

    return render(request, 'user_info_form.html', {'form': form})