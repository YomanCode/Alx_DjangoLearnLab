from django.http import HttpResponseForbidden

def role_required(role):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            if request.user.role == role:
                return func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("You do not have permission to view this page.")
        return wrapper
    return decorator
