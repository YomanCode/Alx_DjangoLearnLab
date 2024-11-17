from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Custom register view
    path('register/', views.register, name='register'),

    # Authentication views
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

    # Role-based views
    path('admin-view/', views.admin_view, name='admin-view'),
    path('librarian-view/', views.librarian_view, name='librarian-view'),
    path('member-view/', views.member_view, name='member-view'),
]
