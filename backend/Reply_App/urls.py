from django.urls import path
from . import views


urlpatterns = [
    # path('videos/', views.reply_list),
    path('reply/<int:pk>/' , views.reply_detail),
]