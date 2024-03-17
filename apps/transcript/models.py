from django.db import models
from uuid import uuid4

# Create your models here.
class Transcript(models.Model):
    
    id = models.UUIDField(primary_key=True, editable=False)
    link_id = models.CharField(max_length=255)
    transcript = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.linkw