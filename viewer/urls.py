from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('channel/<str:name>/', views.post_list, name="post_list")
]
