from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.user.username


class ChatRoom(models.Model):
    name = models.CharField(max_length=100)
    participants = models.ManyToManyField(User, related_name='chatrooms')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username}: {self.content[:30]}"

