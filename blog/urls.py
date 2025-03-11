from django.urls import path,include
from django.contrib.auth.views import LogoutView
from . import views
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

urlpatterns = [
    path('posts', views.post_list, name='post_list'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('signup/', views.signup_view, name='signup'),  
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
