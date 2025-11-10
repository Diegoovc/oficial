from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# Diccionario global donde se guardan los votos y votantes
CATEGORIAS = {
    "Más Gitano/a": {},
    "Más Borracho/a": {},
    "Mejor Grupo": {}
}

# Ejemplo de estructura interna:
# {
#   "Más Gitano/a": {
#       "David": {"votos": 2, "votantes": ["Diego", "Óscar"]}
#   },
#   "Más Borracho/a": {...}
# }

@csrf_exempt
def votar(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        if not nombre:
            return render(request, "form.html", {"error": "Por favor, introduce tu nombre."})

        # 🔹 Coinciden con los 'name' en form.html
        mapping = {
            "Más Gitano/a": request.POST.get("mas_gitano"),
            "Más Borracho/a": request.POST.get("mas_borracho"),
            "Mejor Grupo": request.POST.get("mejor_grupo"),
        }

        # Procesamos cada categoría
        for categoria, opcion in mapping.items():
            if opcion:  # si el usuario ha elegido algo
                if opcion not in CATEGORIAS[categoria]:
                    CATEGORIAS[categoria][opcion] = {"votos": 0, "votantes": []}

                # Evitar votos duplicados por nombre
                if nombre not in CATEGORIAS[categoria][opcion]["votantes"]:
                    CATEGORIAS[categoria][opcion]["votos"] += 1
                    CATEGORIAS[categoria][opcion]["votantes"].append(nombre)

        return redirect("resultados")

    return render(request, "form.html")


def resultados(request):
    return render(request, "resultados.html", {"categorias": CATEGORIAS})
