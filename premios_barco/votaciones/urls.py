from django.urls import path
from . import views

# 1. AÑADE ESTA LÍNEA para definir el namespace
app_name = 'votaciones' 

urlpatterns = [
    path('', views.index, name='index'), 
    path('votar/', views.votar, name='votar'),
    path('resultados/', views.resultados, name='resultados'),
]
# Opcional, pero recomendado
app_name = 'votaciones' 

urlpatterns = [
    # AÑADE ESTA LÍNEA para que la URL base (http://127.0.0.1:8000/) funcione
    path('', views.index, name='index'), 
    
    path('votar/', views.votar, name='votar'),
    path('resultados/', views.resultados, name='resultados'),
]