from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('projekt/', views.projekt, name='projekt'),
    path('subory/', views.subory, name='subory'),
    path('foto/', views.foto, name='foto'),
    path('video/', views.video, name='video'),
]