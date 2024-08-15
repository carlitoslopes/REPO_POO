
class Materia:
    def __init__(self, nombre, codigo):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__materia = []
    @property
    def nombre (self):
        return self.__nombre
    @nombre.setter 
    def nombre(self, name):
        self.__nombre = name 
    
    @property 
    def codigo (self):
        return self.__nombre
    @codigo.setter
    def codigo (self, id_cod):
        self.__codigo = id_cod
    
    def agregar_materias(self, material):
        self.__materia.append(material)
    
    def imprimir_materias (self, nombre, codigo):
        print (f"Materia: {self.__nombre}  Cod: {self.__codigo}")
        for mate in self.__materia:
            mate.imprimir_materias()
        
    
    
    