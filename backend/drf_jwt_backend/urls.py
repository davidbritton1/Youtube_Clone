from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/Comment_App/', include('Comment_App.urls')),
    path('api/Reply_App/', include('Reply_App.urls')),
]
