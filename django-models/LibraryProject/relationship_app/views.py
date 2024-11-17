from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def role_required(role):
    def check_role(user):
        if user.is_authenticated:
            return hasattr(user, 'userprofile') and user.userprofile.role == role
        return False
    return user_passes_test(check_role)

@role_required('ADMIN')
def admin_view(request):
    return render(request, 'relationship_app/admin_dashboard.html', {
        'title': 'Admin Dashboard',
        'role': 'Administrator'
    })

@role_required('LIBRARIAN')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_dashboard.html', {
        'title': 'Librarian Dashboard',
        'role': 'Librarian'
    })

@role_required('MEMBER')
def member_view(request):
    return render(request, 'relationship_app/member_dashboard.html', {
        'title': 'Member Dashboard',
        'role': 'Member'
    })