from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

# Helper functions for role checks
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome, Admin!")

# Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome, Librarian!")

# Member view
@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome, Member!")