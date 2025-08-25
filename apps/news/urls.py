from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='index'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
]