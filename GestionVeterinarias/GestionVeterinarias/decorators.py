from functools import wraps
from django.shortcuts import redirect
from inicio.views import acceso_denegado

def veterinario_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'veterinario':
            return view_func(request, *args, **kwargs)
        else:
            return redirect(acceso_denegado)  # Cambia esto a la página que desees para el acceso denegado
    return _wrapped_view

def no_veterinario_allowed(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role != 'veterinario':
            return view_func(request, *args, **kwargs)
        else:
            return redirect(acceso_denegado)  # Cambia esto a la página que desees para el acceso denegado
    return _wrapped_view

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Verifica si el usuario está autenticado y es un administrador
        if request.user.is_authenticated and request.user.role == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            # Si el usuario no es un administrador, puedes redirigirlo a una página de acceso denegado o a donde desees
            return redirect(acceso_denegado)  # Cambia esto a la página que desees para el acceso denegado
    return _wrapped_view

def no_admin_allowed(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Verifica si el usuario está autenticado y no es un administrador
        if not request.user.is_authenticated or request.user.role != 'admin':
            return view_func(request, *args, **kwargs)
        else:
            # Si el usuario es un administrador, puedes redirigirlo a una página de acceso denegado o a donde desees
            return redirect(acceso_denegado)  # Cambia esto a la página que desees para el acceso denegado
    return _wrapped_view