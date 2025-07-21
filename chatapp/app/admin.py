from django.contrib import admin
from django.contrib.auth.models import User
from .models import  UserInfo, ChatRoom, Message

# Register your models here.

admin.site.register(UserInfo)
admin.site.register(ChatRoom)
admin.site.register(Message)