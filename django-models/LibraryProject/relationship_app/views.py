from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login view - Using Django's built-in view
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout view - Using Django's built-in view
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'