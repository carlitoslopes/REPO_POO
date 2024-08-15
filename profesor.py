
class Profesor:
    
    def __init__(self, nombre_pro, apellido_pro):
        self.__nombre_pro = nombre_pro
        self.__apellido_pro = apellido_pro
        self.__materia = []
    @property#get
    def nombre (self):
        return self.__nombre_pro 
    @property 
    def apellido (self):
        return self.__apellido_pro
    @nombre.setter#set
    def nombre (self, name):
        self.__nombre_pro = name
    @apellido.setter
    def apellido (self, apell):
        self.__apellido = apell
        
    def agregar_materias(self, material):
        self.__materia.append(material)
        
    def imprimir_materias (self, nombre, codigo):
        print (f"Materia: {self.__nombre}  Cod: {self.__codigo}")
        for mate in self.__materia:
            mate.imprimir_materias()
                
    def imprimir_profes (self,nombre_pro, apelido_pro):
        print(f"Profesor: {self.__nombre_pro} {self.__apellido_pro} ")
    
    
    