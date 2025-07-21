from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views 

urlpatterns = [
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
