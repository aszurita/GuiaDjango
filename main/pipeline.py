from django.contrib.auth.models import Group


def add_user_to_group(backend, user, response, *args, **kwargs):
    if backend.name == "google-oauth2":
        group, _ = Group.objects.get_or_create(name="Google Users")
        user.groups.add(group)
        if user.email in ["angelozurita7@gmail.com"]:
            admin_group, _ = Group.objects.get_or_create(name="Administrador")
            user.groups.add(admin_group)
from django.contrib.auth.models import Group
grupo = Group.objects.get(name="Administrador")  # Cambia el nombre por el grupo que quieras
for permiso in grupo.permissions.all():
    print(permiso.codename, permiso.name)
