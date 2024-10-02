
from films import Films
import random
class Series(Films):
    def __init__(self, nombre, año_emision, calificacion):
        super().__init__(nombre, año_emision, calificacion)
        self._capitulos = []
        
        
    def _agregar_capitulos(Self):
        capitulos = random.randint(1,10)
        
        for i in range(capitulos):
            Self._capitulos.append(i)
            opcion = random.randint(0,1)
            print(f"CAPITULO: {i}")
            if opcion == 0:
                print("visto ✅")
            elif opcion == 1:
                print("no visto❎")
            
            
        
    def ficha_multimedia(self):
        super().ficha_multimedia()
        print(f"--------CAPITULOS------------")
        self._agregar_capitulos()
