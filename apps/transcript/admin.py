from django.contrib import admin

from .models import *

@admin.register(Transcript)
class TranscriptAdmin(admin.ModelAdmin):
    pass