from django.urls import path
from . import views


urlpatterns = [
    # path('videos/', views.reply_list),
    path('<int:pk>/' , views.reply_detail),
    path('ADD', views.add_record)
]