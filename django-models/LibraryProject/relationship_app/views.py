# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from .models import UserProfile

def role_required(role):
    def check_role(user):
        if user.is_authenticated:
            return hasattr(user, 'userprofile') and user.userprofile.role == role
        return False
    return user_passes_test(check_role)

@login_required
@role_required('ADMIN')
def admin_view(request):
    """
    Enhanced admin dashboard view with user management capabilities.
    Only accessible to users with the Admin role.
    """
    try:
        # Get query parameters for filtering and pagination
        search_query = request.GET.get('search', '')
        page_number = request.GET.get('page', 1)
        role_filter = request.GET.get('role', '')

        # Base queryset for users
        users = User.objects.select_related('userprofile').all()

        # Apply filters
        if search_query:
            users = users.filter(
                Q(username__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query)
            )

        if role_filter:
            users = users.filter(userprofile__role=role_filter)

        # Sort users by username
        users = users.order_by('username')

        # Pagination
        paginator = Paginator(users, 10)  # 10 users per page
        page_obj = paginator.get_page(page_number)

        # System statistics
        stats = {
            'total_users': User.objects.count(),
            'total_admins': UserProfile.objects.filter(role='ADMIN').count(),
            'total_librarians': UserProfile.objects.filter(role='LIBRARIAN').count(),
            'total_members': UserProfile.objects.filter(role='MEMBER').count(),
        }

        context = {
            'page_obj': page_obj,
            'stats': stats,
            'search_query': search_query,
            'role_filter': role_filter,
            'roles': UserProfile.ROLE_CHOICES,
            'title': 'Admin Dashboard',
            'role': 'Administrator'
        }

        return render(request, 'relationship_app/admin_dashboard.html', context)

    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('home')

@login_required
@role_required('LIBRARIAN')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_dashboard.html', {
        'title': 'Librarian Dashboard',
        'role': 'Librarian'
    })

@login_required
@role_required('MEMBER')
def member_view(request):
    return render(request, 'relationship_app/member_dashboard.html', {
        'title': 'Member Dashboard',
        'role': 'Member'
    })