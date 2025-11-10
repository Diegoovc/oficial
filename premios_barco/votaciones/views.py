# votaciones/views.py

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse # Necesario para construir la URL de redirección

# Diccionario global donde se guardan los votos y votantes
CATEGORIAS = {
    "Más Gitano/a": {},
    "Más Borracho/a": {},
    "Mejor Grupo": {}
}

def index(request):
    """
    Muestra el formulario principal (form.html) y verifica si hay un mensaje de éxito
    pasado a través de la URL.
    """
    context = {}
    
    # 👈 Lógica para capturar el mensaje de éxito de la URL
    if 'success' in request.GET and request.GET['success'] == '1':
        context['success_message'] = "¡Gracias! Tu voto ha sido registrado correctamente."
    
    # Renderiza la plantilla con el contexto (error o éxito)
    return render(request, "form.html", context)


@csrf_exempt
def votar(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        
        if not nombre:
            # Si hay error, renderiza el formulario con el mensaje
            return render(request, "form.html", {"error": "Por favor, introduce tu nombre."})

        # 🔹 Coinciden con los 'name' en form.html
        mapping = {
            "Más Gitano/a": request.POST.get("mas_gitano"),
            "Más Borracho/a": request.POST.get("mas_borracho"),
            "Mejor Grupo": request.POST.get("mejor_grupo"),
        }

        # Procesamos cada categoría
        for categoria, opcion in mapping.items():
            if opcion:
                if opcion not in CATEGORIAS[categoria]:
                    CATEGORIAS[categoria][opcion] = {"votos": 0, "votantes": []}

                # Evitar votos duplicados por nombre
                if nombre not in CATEGORIAS[categoria][opcion]["votantes"]:
                    CATEGORIAS[categoria][opcion]["votos"] += 1
                    CATEGORIAS[categoria][opcion]["votantes"].append(nombre)

        # 👈 LÍNEA CLAVE: Redirige de vuelta a la vista 'index' 
        # y añade el parámetro '?success=1' para mostrar el mensaje de confirmación.
        return redirect(reverse("votaciones:index") + "?success=1")

    # Si se intenta acceder por GET a /votar/ (lo cual no debería ocurrir), redirige al index.
    return redirect("votaciones:index") 


def resultados(request):
    """
    Muestra la tabla con los resultados de la votación.
    """
    return render(request, "resultados.html", {"categorias": CATEGORIAS})