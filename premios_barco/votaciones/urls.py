from django.urls import path
from . import views

urlpatterns = [
    path('votar/', views.votar, name='votar'),
    path('resultados/', views.resultados, name='resultados'),
]