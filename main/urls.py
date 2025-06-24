from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout_view, name="logout"),
    path("oauth/", include("social_django.urls", namespace="social")),
    path("admin_panel/", views.admin_panel, name="admin_panel"),
]
