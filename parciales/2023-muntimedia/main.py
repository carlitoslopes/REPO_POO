from peliculas import Peliculas
from series import Series
from usuario import Usuario
import random

#One Pice (2023) 4 estrellas
#Usted se quedo en DareDevil capitulo 1
#Marveles (2023) 3 estrellas
#Mortal Kombat (2021) 2 estrellas
#Scarface (1983) 5 estrellas
pelicula = ["MORTAL KOMBAT","SCARFACE","POKEMON","LA TRAMPA"]
serie = ["ONE PIECE","LOS UNICOS","DAREDEVIL","COBRA KAI"]
años = [1994,2000,2023,2024,2011,2012]

lista_pelis = []
lista_serie = []

usuario= Usuario("carlos","lopes","carlos-lopes52@hotmail.com","pity1234")

for i in range(0,10):
    lista_pelis.append(Peliculas(random.choice(pelicula),random.choice(años),random.randint(1,5)))
    lista_serie.append(Series(random.choice(serie),random.choice(años),random.randint(1,5)))
    
for i in range(0,5):   
    usuario.añadir_peliculas(lista_pelis[i])
    usuario.añadir_series(lista_serie[i])

usuario.mostrar_usuario()


