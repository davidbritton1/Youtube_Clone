from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_all_comments),
    path('<int:pk>/', views.user_comments),
    path('ADD',views.add_record ),
]