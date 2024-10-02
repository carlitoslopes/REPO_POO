
from films import Films
import random
class Peliculas(Films):
    def __init__(self, nombre, año_emision, calificacion):
        super().__init__(nombre, año_emision, calificacion)
        self._duracion = self._duracion_pelicula()
        
    
    def _duracion_pelicula(self):
        self._duracion = random.randint(60,200)
        return self._duracion
    

            
    
    def ficha_multimedia(self):
        super().ficha_multimedia()
        print(f"DURACION : {self._duracion} MIN")
        
        