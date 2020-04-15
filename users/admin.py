from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email','fname','lname','organization', 'is_staff', 'is_active',)
    list_filter = ('email','organization', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password','fname','lname','organization')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email','organization')
    ordering = ('organization',)


admin.site.register(CustomUser, CustomUserAdmin)