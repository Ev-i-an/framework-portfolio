from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate_blog', views.generate_blog, name='generate-blog'),
    path('blog-list', views.blog_list, name='blog-list'),
    path('blog-details/<int:pk>/', views.blog_details, name='blog-details'),
]