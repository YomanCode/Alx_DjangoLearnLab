from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..decorators import role_required

@login_required
@role_required('MEMBER')
def member_view(request):
    context = {
        'title': 'Member Dashboard',
        'message': 'Welcome to the Member Dashboard',
        'member_features': [
            'Browse Books',
            'My Borrowed Books',
            'Reading History',
            'Book Reservations',
        ]
    }
    return render(request, 'member_dashboard.html', context)