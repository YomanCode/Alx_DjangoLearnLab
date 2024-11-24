from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..decorators import role_required

@login_required
@role_required('LIBRARIAN')
def librarian_view(request):
    context = {
        'title': 'Librarian Dashboard',
        'message': 'Welcome to the Librarian Dashboard',
        'librarian_features': [
            'Book Management',
            'Issue/Return Books',
            'Member Management',
            'Book Reservations',
        ]
    }
    return render(request, 'librarian_dashboard.html', context)