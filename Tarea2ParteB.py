import wikipediaapi
import re
import unidecode

#sacare palabras de una pagina de wikipedia utilzando su API

user_agent ="diccionario (https://github.com/FMM28/diccionario)"
wiki_wiki = wikipediaapi.Wikipedia(user_agent=user_agent,language='es')

page = wiki_wiki.page("México")

datos = page.text.split()
diccionario=[]

for i in datos:
    i=i.lower()
    #utilizo la libreria re para poder eliminar signos de puntuacion y despues la libreria unicode para eliminar los acentos
    i=unidecode.unidecode(re.sub(r'[^A-Za-záéíóúüñÁÉÍÓÚÜÑ]','',i))

    if not i in diccionario:
        diccionario.append(i)

print(len(diccionario))
# print(diccionario)

with open("diccionario.txt",'w') as archivo:
    for i in diccionario:
        archivo.write(i+" ")