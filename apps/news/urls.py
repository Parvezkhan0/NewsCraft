from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='index'),  # Changed from views.index to views.article_list
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),  # Also changed pk to article_id to match your view
]