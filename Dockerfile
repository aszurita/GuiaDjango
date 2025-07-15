# Etapa de build: instalar dependencias y recolectar estáticos
FROM python:3.11-slim AS build

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

# Etapa runtime: imagen ligera con Nginx y Gunicorn
FROM python:3.11-slim AS runtime

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    nginx \
    && rm -rf /var/lib/apt/lists/*

COPY --from=build /app /app

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN echo 'server { \
    listen 8080; \
    server_name localhost; \
    location /static/ { \
        alias /app/static/; \
        expires 30d; \
        add_header Cache-Control "public, max-age=2592000"; \
    } \
    location / { \
        proxy_pass http://unix:/tmp/gunicorn.sock; \
        proxy_set_header Host $host; \
        proxy_set_header X-Real-IP $remote_addr; \
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; \
        proxy_set_header X-Forwarded-Proto $scheme; \
    } \
}' > /etc/nginx/conf.d/default.conf

EXPOSE 8080

CMD gunicorn backend.wsgi:application \
        --bind unix:/tmp/gunicorn.sock \
        --workers 3 & \
    nginx -g 'daemon off;'
