from django.urls import path
from . import views


urlpatterns = [
    path('comments/', views.get_all_comments),
    path('comments/<int:pk>/' , views.user_comments),
]