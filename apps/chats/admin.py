from django.contrib import admin
# Models
from .models import *


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('link_id', 'prompt', 'user_id')
    readonly_fields = ('link_id', 'id', 'created_at', 'updated_at')

    fieldsets = (
        ('Chat Details', {'fields': ('id', 'link_id', 'prompt', 'message', 'user')}), (
            'Timestamps', {'fields': ('created_at', 'updated_at')}
        )
    )
