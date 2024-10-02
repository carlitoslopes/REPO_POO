#Se tiene una plataforma de streaming llamada el Video Amigo. De un usuario de la
#plataforma se conoce el nombre, apellido, mail y password.
import random
from films import Films

class Usuario: 
    def __init__(self,nombre,apellido,mail,contraseña):
        self._nombre = nombre
        self._apellido = apellido
        self._mail = mail
        self._contraseña = contraseña
        self._peliculas = []
        self._series = []
        
    
    def añadir_peliculas(self,pelis):
            self._peliculas.append(pelis)
            
    def añadir_series(self,serie):
            self._series.append(serie)
            
            

        
        
    def mostrar_usuario(self):
        print("🎬🎬🎬🎬🎬🎬🎬🎬🎬 VIDEO AMIGO 🎬🎬🎬🎬🎬🎬🎬🎬🎬")
        print(f"NOMBRE : {self._nombre}")
        print(f"APELLIDO: {self._apellido}")
        print(f"MAIL: {self._mail}")
        print(f"CONTRASEÑA {self._contraseña}")
        print("________________________________")
        print("PELICULAS FAVORITAS 🎞️")
        print("")
        for i in self._peliculas:
            i.ficha_multimedia()
            print("=======================")
        print("________________________________")
        print("SERIES FAVORITAS 🎞️ ")
        print("")
        for j in self._series:
            j.ficha_multimedia()
            
            print("=======================")
            
            
        
        
        