from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin-dashboard/', admin_view, name='admin-dashboard'),
    path('librarian-dashboard/', librarian_view, name='librarian-dashboard'),
    path('member-dashboard/', member_view, name='member-dashboard'),
]