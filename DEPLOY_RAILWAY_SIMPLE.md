# 🚀 Deploy Súper Simple en Railway

## ✅ Configuración AUTOMÁTICA

Tu app ya está lista! No necesitas configurar base de datos ni nada complicado:

- **📱 Local**: Sigue usando SQLite como siempre
- **☁️ Railway**: Automáticamente detecta y usa PostgreSQL
- **🔧 Variables**: Solo 2 variables obligatorias

## 📋 Pasos de Deploy (5 minutos)

### 1. Sube tu código a GitHub

```bash
git add .
git commit -m "Configurado para Railway"
git push
```

### 2. Crea proyecto en Railway

1. Ve a [railway.app](https://railway.app)
2. "New Project" → "Deploy from GitHub repo"
3. Selecciona tu repositorio

### 3. Agrega PostgreSQL

1. En Railway, click "Create" → "Database" → "Add PostgreSQL"
2. ¡Listo! Railway conecta automáticamente

### 4. Configura SOLO 2 variables obligatorias

En la pestaña "Variables" de tu servicio Django:

```
SECRET_KEY=genera-uno-nuevo-aqui
DEBUG=False
```

**Genera tu SECRET_KEY:**

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Deploy y Dominio

1. Click "Deploy"
2. Ve a "Networking" → "Generate Domain"
3. ¡Tu app está online! 🎉

## 🤔 Variables Opcionales

**Solo si usas Google OAuth:**

```
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=tu-google-client-id
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=tu-google-client-secret
```

## ⚙️ ¿Qué hace automáticamente?

- ✅ Detecta si está en Railway o local
- ✅ Usa SQLite local, PostgreSQL en Railway
- ✅ Configura archivos estáticos con WhiteNoise
- ✅ Ejecuta migraciones automáticamente
- ✅ Modo DEBUG False en producción

## 🔍 Troubleshooting

**Error en deploy:**

1. Verifica que agregaste la base de datos PostgreSQL
2. Verifica que configuraste `SECRET_KEY` y `DEBUG=False`
3. Mira los logs en Railway Dashboard

**Google OAuth no funciona:**

1. En Google Console, agrega tu dominio Railway a URLs autorizadas
2. Configura las variables `SOCIAL_AUTH_GOOGLE_OAUTH2_*`

¡Eso es todo! 🚀 Tu Django app funcionará igual localmente y en producción.
