from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from accounts.forms import CustomUserCreationForm, CUstomUserChangeForm
from accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CUstomUserChangeForm
    list_display = ('email', 'username')

# admin.site.register(CustomUser, CustomUserAdmin)
