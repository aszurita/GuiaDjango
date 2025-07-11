import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "backend.settings"
)  # Ajusta si necesario
django.setup()

from django.contrib.auth.models import User, Group

administradores = [
    {
        "username": "angelozurita7",
        "email": "angelozurita7@gmail.com",
        "first_name": "Angelo",
        "last_name": "Zurita",
    },
    {
        "username": "nzuritag",
        "email": "nzuritag@fiec.espol.edu.ec",
        "first_name": "Zurita",
        "last_name": "Guerrero",
    },
]

grupo_admin, _ = Group.objects.get_or_create(name="Administrador")

for admin in administradores:
    user, created = User.objects.get_or_create(
        username=admin["username"],
        defaults={
            "email": admin["email"],
            "first_name": admin["first_name"],
            "last_name": admin["last_name"],
            "is_active": True,
        },
    )
    user.email = admin["email"]
    user.first_name = admin["first_name"]
    user.last_name = admin["last_name"]
    user.is_staff = True
    user.is_superuser = True
    user.groups.add(grupo_admin)
    user.save()

print("Administradores cargados correctamente.")
