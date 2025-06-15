from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from social_django.models import UserSocialAuth


def index(request):
    user = request.user
    social_auth = None
    if user.is_authenticated:
        social_auth = user.social_auth.first()
    context = {
        'user': user,
        'social_auth': social_auth
    }
    return render(request, 'main/index.html', context)

def login(request):
    return render(request, 'main/login.html')

@login_required
def profile(request):
    user = request.user
    social_auth = user.social_auth.first()
    context = {
        'user': user,
        'social_auth': social_auth
    }
    return render(request, 'main/profile.html', context)

def logout_view(request):
    # Eliminar la sesión social si existe
    if request.user.is_authenticated:
        UserSocialAuth.objects.filter(user=request.user).delete()
    # Cerrar la sesión de Django
    logout(request)
    # Redirigir al login
    return redirect('index')



# Ciertos usuarios me dijirian a una pagina y a otra pagina