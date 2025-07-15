from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
import logging

logger = logging.getLogger(__name__)
User = get_user_model()


def connect_by_email(backend, uid, user=None, *args, **kwargs):
    """
    Pipeline personalizado para conectar usuarios por email
    """
    try:
        # Si ya hay un usuario, no hacer nada
        if user:
            logger.info(f"Usuario ya existe en el pipeline: {user.email}")
            return None 

        # Obtener detalles del usuario desde Google
        details = kwargs.get("details", {})
        email = details.get("email")
        first_name = details.get("first_name", "")
        last_name = details.get("last_name", "")
        username = kwargs.get("username") or (email.split("@")[0] if email else "")

        logger.info(f"Procesando autenticación para: {email}")

        # Validar que tenemos un email
        if not email:
            logger.error("No se encontró email en los detalles del usuario de Google")
            return None 

        try:
            # Buscar si el usuario ya existe por email
            existing_user = User.objects.get(email=email)
            logger.info(f"Usuario existente encontrado: {existing_user.email}")
            return {"user": existing_user}

        except User.DoesNotExist:
            logger.info(f"Creando nuevo usuario para: {email}")
            
            # Generar username único si ya existe
            original_username = username
            counter = 1
            while User.objects.filter(username=username).exists():
                username = f"{original_username}{counter}"
                counter += 1
            
            # Crear nuevo usuario
            new_user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                is_active=True,
            )

            # Asignar a grupo de usuarios de Google
            google_group, created = Group.objects.get_or_create(name="Google Users")
            new_user.groups.add(google_group)
            new_user.save()

            logger.info(f"Usuario creado exitosamente: {new_user.email} con username: {new_user.username}")
            return {"user": new_user}
            
    except Exception as e:
        logger.error(f"Error crítico en pipeline connect_by_email: {str(e)}")
        logger.exception("Detalles del error:")
        # Retornar None para que continúe con el pipeline normal de Django
        return None