from django.db import models


# Create your models here.
class Permisos(models.Model):  # puede ser cualquier modelo real o ficticio
    class Meta:
        permissions = [
            ("acceso_admin_panel", "Puede acceder al panel de administración"),
            ("acceso_solo_Usuarios", "Puede acceder a informacion de solo Usurios"),
        ]
