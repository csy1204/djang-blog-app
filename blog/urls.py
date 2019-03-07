from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog_list, name='blog'),
    path('view/<int:pk>', views.blog_view, name='blog_view'),
    path('new', views.blog_new, name='blog_new'),
    path('create', views.blog_create, name='blog_create'),
    path('edit/<int:pk>', views.blog_update, name='blog_edit'),
    path('delete/<int:pk>', views.blog_delete, name='blog_delete'),
    path('newblog/', views.blogpost, name= 'newblog'),
]