from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UsersCreationForm, UsersChangeForm
from .models import User

# Register your models here.


class UsersAdmin(UserAdmin):
    add_form = UsersCreationForm
    form = UsersChangeForm
    model = User
    list_display = ['first_name', 'last_name', 'email']


admin.site.register(User, UsersAdmin)