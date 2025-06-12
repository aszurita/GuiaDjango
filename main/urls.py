from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='main_index'),
    path('login/', views.login, name='login'),
    path('', include('social_django.urls', namespace='social')),
]