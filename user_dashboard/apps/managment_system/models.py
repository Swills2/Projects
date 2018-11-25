from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    description = models.TextField(max_length=1000, null=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)

class Message(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    for_user = models.ForeignKey(User, related_name='messages_recieved', on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, related_name='messages_sent', on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    from_user = models.ForeignKey(User, related_name='comments_sent', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name='comments', on_delete=models.CASCADE)

    