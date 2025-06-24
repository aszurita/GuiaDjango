from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission, Group


def add_user_to_group(backend, user, response, *args, **kwargs):
    if backend.name == "google-oauth2":
        group, _ = Group.objects.get_or_create(name="Google Users")
        user.groups.add(group)
        if user.email in ["angelozurita7@gmail.com", "nzuritag@fiec.espol.edu.ec"]:
            admin_group, _ = Group.objects.get_or_create(name="Administrador")
            user.groups.add(admin_group)
