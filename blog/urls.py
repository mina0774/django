from django.urls import path
from django.contrib import admin
from django.contrib.auth import views
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('menu/<int:pk>/',views.menu_detail,name='menu_detail'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('menu/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/',views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/remove/',views.comment_remove,name="comment_remove"),
    path('comment/<int:pk>/approve/',views.comment_approve,name="comment_approve"),
    path('result/',views.result,name='result'),
]
