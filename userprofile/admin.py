from django.contrib import admin
from .models import user_info

@admin.register(user_info)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['N_id', 'Name', 'email', 'Education_Level', 'Phone_no', 'School']
