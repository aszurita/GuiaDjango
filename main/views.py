from django.contrib.auth import logout
from social_django.models import UserSocialAuth
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render

def index(request):
    user = request.user
    social_auth = None
    if user.is_authenticated:
        social_auth = user.social_auth.first()
    context = {"user": user, "social_auth": social_auth}
    return render(request, "main/index.html", context)


def login(request):
    return render(request, "main/login.html")


@login_required
def profile(request):
    user = request.user
    social_auth = user.social_auth.first()
    is_admin = request.user.groups.filter(name="Administrador").exists()
    context = {"user": user, "social_auth": social_auth, "is_admin": is_admin}
    return render(request, "main/profile.html", context)


def logout_view(request):
    # Eliminar la sesión social si existe
    if request.user.is_authenticated:
        UserSocialAuth.objects.filter(user=request.user).delete()
    # Cerrar la sesión de Django
    logout(request)
    # Redirigir al login
    return redirect("index")


@login_required
@permission_required("main.acceso_admin_panel", raise_exception=True)
def admin_panel(request):
    return render(request, "main/admin_panel.html")


def error_403_view(request, exception=None):
    return render(request, "main/403.html", status=403)
