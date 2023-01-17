"""
El siguiente programa tiene como objetivo imprimir una lista de caracteres y devolver 
el que no se repita de cada uno

Autores:
Jose Sanmartin
Verisión:
VER.0.1
"""
#Importamos las librerias que vamos a utilizar durante el programa 
import os, big_o, random,string
def cadena_CaracteresnoR(numero_palabras):
    """
    Esta función recoge diversas frases y recorre la misma con la finalidad
    de hallar cual es la primera letra que no se repite.
    Parametros:
        Recoge como parametros una cadena de caracteres
    Retorno:
        No tiene retorno
    """
    #Se ingresa el numero de palabras que se quiere generar
    numero_palabras=int(input("Ingrese el numero de palabras a generar: ")) 
    #se crea cuantos caracateres tiene cada palabra 
    numeroCaracteres=int(input("Ingrese la longitud de los caracteres: "))
    #Empezamos a generear las cadenas de caracteres en este caso cuantas 
    for x in range(numero_palabras):
        #creamos la manera en que se crearan los caracteres 
        cadenas=(''.join(random.choice(string.ascii_letters) 
        #creamos la cadena con sus elementos 
        for i in range(numeroCaracteres)))
        #enlistamos las cadenas 
        lista=(list(cadenas))
        #retorna las listas 
        return lista
        


    

if __name__ == "__main__":
    # iterador establecido en 0
    i = 0
    #Se ingresa el numero de palabras que se quiere generar
    numero_palabras=int(input("Ingrese el numero de palabras a generar: ")) 
    #se crea cuantos caracateres tiene cada palabra 
    numeroCaracteres=int(input("Ingrese la longitud de los caracteres: "))
    cadenas = cadena_CaracteresnoR(numero_palabras)

    for i in range(numero_palabras):
        una_cadena = lambda c: cadenas[i]
        best, others = big_o.big_o(cadena_CaracteresnoR,una_cadena)
        print(cadena_CaracteresnoR)
    
    print(best)

