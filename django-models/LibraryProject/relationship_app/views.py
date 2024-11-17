from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse

def check_admin(user):
    return user.is_authenticated and user.userprofile.role == 'ADMIN'

def check_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'LIBRARIAN'

def check_member(user):
    return user.is_authenticated and user.userprofile.role == 'MEMBER'

@login_required
@user_passes_test(check_admin)
def admin_view(request):
    context = {
        'title': 'Admin Dashboard',
        'user': request.user,
        'admin_actions': [
            'Manage Users',
            'View System Logs',
            'Configure Settings',
            'Manage Roles'
        ]
    }
    return render(request, 'admin_dashboard.html', context)

@login_required
@user_passes_test(check_librarian)
def librarian_view(request):
    context = {
        'title': 'Librarian Dashboard',
        'user': request.user,
        'librarian_actions': [
            'Manage Books',
            'Handle Loans',
            'Process Returns',
            'Manage Reservations'
        ]
    }
    return render(request, 'librarian_dashboard.html', context)

@login_required
@user_passes_test(check_member)
def member_view(request):
    context = {
        'title': 'Member Dashboard',
        'user': request.user,
        'member_actions': [
            'Browse Books',
            'View Loans',
            'Make Reservations',
            'View History'
        ]
    }
    return render(request, 'member_dashboard.html', context)

@login_required
def home_view(request):
    """Redirects users to their appropriate dashboard based on their role."""
    role = request.user.userprofile.role
    
    if role == 'ADMIN':
        return HttpResponseRedirect(reverse('admin_dashboard'))
    elif role == 'LIBRARIAN':
        return HttpResponseRedirect(reverse('librarian_dashboard'))
    else:
        return HttpResponseRedirect(reverse('member_dashboard'))
