from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()


def connect_by_email(backend, uid, user=None, *args, **kwargs):
    if user:
        return None 

    email = kwargs.get("details", {}).get("email")
    first_name = kwargs.get("details", {}).get("first_name", "")
    last_name = kwargs.get("details", {}).get("last_name", "")
    username = kwargs.get("username") or email.split("@")[0]

    if not email:
        return None 

    try:
        user = User.objects.get(email=email)
        return {"user": user}

    except User.DoesNotExist:
        print("Usuario no existe, creando usuario")
        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_active=True,
        )

        group, _ = Group.objects.get_or_create(name="Google Users")
        user.groups.add(group)
        user.save()

        return {"user": user}