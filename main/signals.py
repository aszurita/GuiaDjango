from django.db.models.signals import post_migrate
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from django.apps import apps


@receiver(post_migrate)
def crear_permiso_admin(sender, **kwargs):
    DummyModel = apps.get_model("main", "DummyModel")  # o el modelo real que usaste
    content_type = ContentType.objects.get_for_model(DummyModel)

    perm, created = Permission.objects.get_or_create(
        codename="acceso_admin_panel",
        name="Puede acceder al panel de administración",
        content_type=content_type,
    )
    grupo, _ = Group.objects.get_or_create(name="Administrador")
    grupo.permissions.add(perm)
