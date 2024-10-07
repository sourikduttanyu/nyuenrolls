from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import StudentInfo
 
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        # Include all fields
        fields = ['N_id', 'Name', 'email', 'Education_Level', 'Phone_no', 'School']

        # You can customize widgets here if needed
        widgets = {
            'Education_Level': forms.Select(),
            'School': forms.Select(),
        }

class create_user_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

