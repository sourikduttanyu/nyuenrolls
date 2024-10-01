from django import forms
from .models import user_info

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = user_info
        # Include all fields
        fields = ['N_id', 'Name', 'email', 'Education_Level', 'Phone_no', 'School']

        # You can customize widgets here if needed
        widgets = {
            'Education_Level': forms.Select(),
            'School': forms.Select(),
        }