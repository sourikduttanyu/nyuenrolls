from django.contrib import admin
from .models import StudentInfo

@admin.register(StudentInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['N_id', 'Name', 'email', 'Education_Level', 'Phone_no', 'School']
