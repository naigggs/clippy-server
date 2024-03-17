from uuid import uuid4
from django.db import models

class Chat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    
    # Chat Details
    link_id = models.CharField(max_length=255, blank=True, null=True)
    prompt = models.TextField(blank=False, null=True)
    message = models.TextField(blank=False, null=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # User 
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='chats', blank=True, null=True, default=None)   

    def __str__(self):
        return self.prompt

    class Meta:
        db_table = 'chats'
        ordering = ['-created_at']
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'

