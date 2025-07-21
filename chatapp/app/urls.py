from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from app.views import *

urlpatterns = [
    path('', indexView, name='index'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('register/', register, name='register'),
]
from django.urls import re_path
from . import consumer

websocket_urlpatterns = [
   re_path(r'ws/chat/(?P<room_id>\w+)/$', consumer.ChatConsumer.as_asgi()),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
