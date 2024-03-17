from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'created_at', 'active', 'staff', 'admin')  
    readonly_fields = ('id', 'created_at')

    fieldsets = (
        ('Auth Information', {
            'fields': ('id', 'username', 'email', 'password')
        }),
        ('Personal Information', {
            'fields': ('profile_picture', 'first_name', 'last_name')
        }),
        ('Permissions', {
            'fields': ('active', 'staff', 'admin')
        }),
         ('Timestamps', {
            'fields': ('created_at',)
        }),
    )

admin.site.register(User, UserAdmin)
