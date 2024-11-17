from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..decorators import role_required

@login_required
@role_required('ADMIN')
def admin_view(request):
    context = {
        'title': 'Admin Dashboard',
        'message': 'Welcome to the Admin Dashboard',
        'admin_features': [
            'User Management',
            'System Configuration',
            'Role Assignment',
            'Audit Logs',
        ]
    }
    return render(request, 'admin_dashboard.html', context)