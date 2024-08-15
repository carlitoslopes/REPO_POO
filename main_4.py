
from materia import Materia
from profesor import Profesor

poo = Materia("POO", "IF153")
algebra = Materia ("Algebra", 183)
introduccion = Materia("Introduccion a la computadora","IF300")
algoritmica = Materia ("Algoritmica",500)

profesor1 = Profesor ("Pedro","hernandez")
profesor1.agregar_materias(poo)
#profesor1.imprimir_profes()
profesor1.imprimir_materias(poo)

#profesores = []

#profesor1.agregar_materias (poo)
#profesores.append(profesor1)
#profesor1.agregar_materias(algebra)
#profesor2 = Profesor ("Romina","Alvarez")
#profesores.append(profesor2)
#profesor2.agregar_materias(introduccion)
#profesor2.agregar_materias(algoritmica)
#profesor3 = Profesor("Laura","Perez")
#profesores.append(profesor3)

