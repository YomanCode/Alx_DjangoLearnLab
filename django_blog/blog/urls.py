from django.urls import path
from . import views

urlpatterns = [
    path("comment/<int:pk>/update/", views.CommentUpdateView.as_view(), name='edit-comment'),
    path("post/<int:pk>/comments/new/", views.add_comment, name='add-comment'),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name='delete-comment'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
