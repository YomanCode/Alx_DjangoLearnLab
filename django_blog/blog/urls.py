from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import RegisterView, profile_view

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profile_view, name='profile'),
    path("comment/<int:pk>/update/", views.CommentUpdateView.as_view(), name='edit-comment'),
    path("post/<int:pk>/comments/new/", views.add_comment, name='add-comment'),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name='delete-comment'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts-by-tag'),
    path('search/', views.PostSearchView.as_view(), name='post-search'),
]
