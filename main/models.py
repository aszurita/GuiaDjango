from django.db import models


# Create your models here.
class DummyModel(models.Model):  # puede ser cualquier modelo real o ficticio
    class Meta:
        permissions = [
            ("acceso_admin_panel", "Puede acceder al panel de administración"),
        ]
