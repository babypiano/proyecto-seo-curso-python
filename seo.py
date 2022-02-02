#Auditoria SEO

from typing import Text
import urllib.request as request #Libreria necesaria para leer la url y el peso del sitio
from urllib.request import urlopen #Importamos solo urlopen, ya que en la linea anterior ya se importo la libreria urllib
from bs4 import BeautifulSoup
import re
import os

print("***Auditoria de HTTPS***")
#************Verificar HTTPS********************
req = request.Request('http://python.org')  #Se debe ingresar HTTP para que valide HTTPS
resultado = request.urlopen(req)
print('***HTTP Or HTTPS: ', resultado.geturl())

#************Peso de la pagina********************
url = "http://python.org"   #Se debe ingresar https para que regrese el peso de la pagina
print("url: ", url)
site = request.urlopen(url)
meta = site.info()
print(" Content-Length: ", site.headers['content-length'])

#************Verificar www********************
req = request.Request('http://python.org')
resultado = request.urlopen(req)
print("***Verificamos si el sitio cuenta con www: ",resultado.geturl())

#************Verificar tamaño de Meta Description********************
site = request.urlopen('https://python.org')
soup = BeautifulSoup(site)
description = soup.find('meta', attrs={'name':'description'})
print('***El tamaño de la Meta descripcion es: ',len(description.get('content')))
if(len(description.get('content')))<154:
    print("***El tamaño de la descripcion es menor a 154 ")

#************Verificar etiqueta title********************
html = urlopen('https://python.org')
soup = BeautifulSoup(html.read())
print("***El tamaño del title es: ", len(soup.html.head.title.string))
print("***El title es: ", soup.html.head.title.string)

#************Detectar palabras clave********************
site = request.urlopen('https://python.org')
soup = BeautifulSoup(site)
keywords = soup.find('meta',attrs={'name': 'keywords'})
print('***Las keywords son: ',keywords.get('content'))
words = keywords.get('content').split()
print(words)
for word in words:
    print(word,len(soup.findAll(text=re.compile(word))))

#************ALT en imagenes********************
site = request.urlopen('http://python.org')
soup = BeautifulSoup(site)
count = 1
for image in soup.findAll('img'):
    print('**Imagen #', count, ":" ,image["src"])
    print(" Alt de imagen #" , count, ":", image.get('alt', 'None'))
    count +=1

#************Detectar encabezados H1********************
site = request.urlopen("http://python.org")
soup = BeautifulSoup(site)
for h1 in soup.findAll('h1'):
    print("***Este es un H1: ",h1)
print("***Total de H1s: ", len(soup.find_all('h1')))

#************Verificar links********************
site = request.urlopen("http://python.org")
soup = BeautifulSoup(site)
links = []
elements = soup.select('a')

for element in elements:
    link = element.get('href')
    if link.startswith('http'):
        links.append(link)
print(links)

for link in links[:5]:
    petition = urlopen(link)
    print("**Enlace: ", link, "Respuesta: ", petition.code)


#************Verificar y descargar favicon********************
url = "http://python.org"
page = request.urlopen(url)
soup = BeautifulSoup(page)
icon_link = soup.find('link',rel="icon")
icon = request.urlopen(url+icon_link['href'])
with open("test.ico","wb") as f:
    try:
        f.write(icon.read())
        print("***¡Se ha detectado y descargado el Favicon exitosamente!***")
    except:
        print("***No de detecto Favicon")


#************Detectar Script de Google Analitics********************
site = request.urlopen("http://python.org")
soup = BeautifulSoup(site)
if(soup.findAll(text=re.compile(".google-analytics.com/ga.js"))):
    print("***Cuenta con Script de Analytics ")
else:
    print("***No cuenta con Script de Analytics")


#************Detectar idioma del sitio********************
site = request.urlopen("http://python.org")
soup = BeautifulSoup(site,'html.parser')
lang = soup.find('html')['lang']
print('***El idioma "lang" del sitio web es: ',lang)

#************Obtener Metadata********************
site = "http://python.org"
print("pagina", site)
peticion = request.urlopen(site)
meta = petition.info()
print(meta)

#************Viewport********************
site = request.urlopen("http://python.org")
soup = BeautifulSoup(site)
print(soup.find('meta',attrs={'name':'viewport'}))

