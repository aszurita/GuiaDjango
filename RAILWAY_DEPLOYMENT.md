# Deployment en Railway

Esta guía te ayudará a deployar tu aplicación Django en Railway.

## Prerrequisitos

Los archivos necesarios ya están configurados:

- ✅ `requirements.txt` actualizado con dependencias de Railway
- ✅ `backend/settings.py` configurado para producción
- ✅ `Procfile` para Railway
- ✅ `runtime.txt` con versión de Python
- ✅ `railway.env.template` con variables de entorno necesarias

## Pasos para Deploy

### 1. Crear cuenta en Railway

Ve a [railway.app](https://railway.app) y crea una cuenta.

### 2. Crear nuevo proyecto

1. En Railway, haz clic en "New Project"
2. Selecciona "Deploy from GitHub repo"
3. Conecta tu repositorio de GitHub

### 3. Agregar Base de Datos PostgreSQL

1. En el canvas del proyecto, haz clic en "Create"
2. Selecciona "Database"
3. Selecciona "Add PostgreSQL"

### 4. Configurar Variables de Entorno

En tu servicio de la app, ve a la sección "Variables" y agrega:

#### Variables obligatorias:

```
SECRET_KEY=tu-secret-key-aqui-genera-uno-nuevo
DEBUG=False
PGDATABASE=${{Postgres.PGDATABASE}}
PGUSER=${{Postgres.PGUSER}}
PGPASSWORD=${{Postgres.PGPASSWORD}}
PGHOST=${{Postgres.PGHOST}}
PGPORT=${{Postgres.PGPORT}}
```

#### Variables opcionales (OAuth Google):

```
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=tu-google-oauth2-key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=tu-google-oauth2-secret
```

### 5. Deploy

1. Haz clic en "Deploy" en tu servicio
2. Railway detectará automáticamente que es una app Django
3. Ejecutará las migraciones y collect static automáticamente

### 6. Generar Dominio Público

1. Ve a la sección "Networking" en Settings
2. Haz clic en "Generate Domain"
3. Tu app estará disponible en la URL generada

## Notas Importantes

1. **SECRET_KEY**: Genera una nueva para producción usando:

   ```python
   from django.core.management.utils import get_random_secret_key
   print(get_random_secret_key())
   ```

2. **OAuth Google**: Si usas autenticación con Google, actualiza las URLs de redirección en Google Console:

   - Authorized origins: `https://tu-dominio-railway.up.railway.app`
   - Authorized redirect URIs: `https://tu-dominio-railway.up.railway.app/complete/google-oauth2/`

3. **Static Files**: Se sirven automáticamente con WhiteNoise

4. **Database**: Las migraciones se ejecutan automáticamente en cada deploy

## Estructura de Archivos Modificados

```
GuiaDjango/
├── backend/
│   └── settings.py          # ✅ Configurado para Railway
├── requirements.txt         # ✅ Dependencias agregadas
├── Procfile                 # ✅ Comando de inicio
├── runtime.txt              # ✅ Versión de Python
├── railway.env.template     # ✅ Variables de entorno
└── RAILWAY_DEPLOYMENT.md    # ✅ Esta guía
```

## Solución de Problemas

1. **Error de migraciones**: Verifica que las variables de base de datos estén correctas
2. **Static files no cargan**: Verifica que `STATIC_ROOT` esté configurado
3. **Error 500**: Revisa los logs en Railway Dashboard > View Logs

¡Tu aplicación Django está lista para Railway! 🚀
