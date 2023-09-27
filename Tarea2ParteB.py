import wikipediaapi

# Crea una instancia de la API de Wikipedia
wiki_wiki = wikipediaapi.Wikipedia('es')  # Cambia 'es' al idioma deseado

# Realiza una búsqueda en Wikipedia
page_title = "Python (programming language)"  # Cambia esto al título de la página que deseas buscar
page = wiki_wiki.page(page_title)

# Verifica si la página existe
if page.exists():
    # Imprime el título y el contenido de la página
    print("Título:", page.title)
    print("Contenido:")
    print(page.text)
else:
    print("La página no existe en Wikipedia.")

# Puedes acceder a otras propiedades de la página, como los enlaces internos o las secciones.
# Por ejemplo, para obtener una lista de enlaces internos:
links = page.links
print("Enlaces internos:")
for link_title in sorted(links.keys()):
    print(link_title)
