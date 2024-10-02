
#Cada usuario puede tener múltiples perfiles. Cada uno de ellos tiene un nombre para
#distinguirlo, si es para niños o no y además una lista de series y películas seleccionadas
#como favoritas. De las series y películas se conoce el nombre, año de emisión y
#calificación medido por estrellas de 1 a 5, siendo 1 mala y 5 muy buena. Las series
#tienen una lista de capítulos con su nombre, orden y si fue visto o no.
#La película tiene un indicador si fue vista o no.
#Tenga en cuenta que tanto película como serie deberá tener un método reproducir y que
#la serie tiene capítulos.

#apellido, nombre
#Perfil : ale

from abc import ABC,abstractmethod
import random
class Films(ABC):
    def __init__(self,nombre,año_emision,calificacion):
        self._nombre = nombre
        self._año_emision = año_emision
        self._calificacion = calificacion
        
    def _reproducir(self):
        opcion = random.randint(1,2)
        match opcion:
            case 1:
                print(f"▶️ reproducir {self._nombre} ")
                print("✅ reproduciendo")
            case 2:
                print(f"⏸️  {self._nombre} pausa")
                print("pausado")
        
    def ficha_multimedia (self):
        print(f"{self._nombre}")
        print(f"AÑO DE EMISION: {self._año_emision} ")
        print(f"CALIFICACION: {self._calificacion} ⭐")
        self._reproducir()
        
    

