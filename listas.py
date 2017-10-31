#encoding: UTF-8
#Autor: Maria Fernanda Torres Velazquez A01746537
#El siguiente programa, realiza diferentes pruebas de operaciones con listas


def sumarDatos (lista): #La funcion recibe una lista como parametro, y va sumando sus elementos, asi regresa una nueva lista con la suma acumulada de los datos
    sumaDatos = 0 #Contador
    listaSuma = [] #Declaracion de la nueva lista

    for i in lista: #i, ira recorriendo cada valor de la lista recibida
        sumaDatos = sumaDatos + i #Ira sumando los valores de la lista
        listaSuma.append(sumaDatos) #Ira llenando la nueva lista con la suma acumulada de los valores

    return (listaSuma)



def quitarElementos(lista): #Funcion que recibe una lista como parametro y devuelve una nueva sin el primer y ultimo elemento de la lista recibida
    newList = lista [:]
    newList.remove(lista[-1])
    newList.remove(lista[0])
    return (newList)

def verListaOrdenada (lista): #La funcion recibe una lista, verifica si esta ordenada y regresa verdadero, de lo contrario, regresa falso
    ordenar = lista[:]
    ordenar.sort()
    if lista == ordenar:
        r=  True
    else:
        r = False
    return (r)

def calcularAnagramas(palabra1,palabra2): #La siguiente funcion recibe 2 cadenas y si son anagramas devuelve true, de lo contrario false
    p1= palabra1.upper() #Transforma la cadena 1 a mayusculas
    p2= palabra2.upper()#Transforma cadena 2 a mayusculas
    list1 = list(p1) #Crea una lista con la cadena 1
    list2 = list(p2) #Crea una lista con la cadena 2
    list1.sort() #Ordena lista 1
    list2.sort() #Ordena lista 2

    if list1 == list2: #Compara si ambas cadenas tienen las mismas palabras ordenadas para ver si son anagramas
        a = True
    else:
        a = False

    return (a)

def verificarValoresRepetidos (lista): #Funcion que recibe una lista y verifica si alguno de sus elementos se repite, si es asi devuelve True, si no False
    nueva= lista[:]
    for x in nueva: #Ira recorriendo cada valor de la lista recibida
        if nueva.count(x) > 1: #Verificara si cada valor se repite
            r= True
        else:
            r= False
        return (r)


def imprimirSoloUnValor (lista): #Funcion que recibe una lista y solo deja 1 valor de cada elemento
    for x in lista:
        while lista.count (x) > 1:
            lista.remove(x)

    return (lista)




def main ():

    #Sumar datos:
    print ("")
    print ("EJERCICIO 1: Recibe una lista con numeros enteros y regresa una nueva lista con la suma acumulada de datos")
    print ("")
    lista = [1, 2, 3, 4, 5]
    nuevaLista1= sumarDatos(lista)
    print("La lista: ", lista, "regresa la lista acumulada: ", nuevaLista1)
    lista2= []
    nuevaLista2= sumarDatos (lista2)
    print("La lista: ", lista2, "regresa la lista acumulada: ", nuevaLista2)
    lista3 = [5]
    nuevaLista3 = sumarDatos(lista3)
    print("La lista: ", lista3, "regresa la lista acumulada: ", nuevaLista3)


    #Quitar elementos:
    print ("")
    print("----------------------------------------------")
    print("EJERCICIO 2: Recibe una lista, y regresa una nueva sin el primer y ultimo elemento de la primera")
    print ("")
    lista4= [1,2,3,4,5]
    listaNueva= quitarElementos(lista4)
    print("Lista original: ", lista4, "regresa: ", listaNueva)
    lista5 = [1,2,3]
    listaNueva2 = quitarElementos(lista5)
    print("Lista original: ", lista5, "regresa: ", listaNueva2)
    lista6 = [1, 2]
    listaNueva3 = quitarElementos(lista6)
    print("Lista original: ", lista6, "regresa: ", listaNueva3)

    #Lista Ordenada
    print ("")
    print("----------------------------------------------")
    print("EJERCICIO 3: Recibe una lista y duveulve el valor TRUE si esta ordenada, en caso contrario, devuelve FALSE")
    print ("")
    lista6 = [1, 2, 3, 4, 5]
    ordenados = verListaOrdenada(lista6)
    print ("Lista", lista6, "esta ordenada - ",ordenados)
    lista7 = [1,5,4]
    ordenados2 = verListaOrdenada(lista7)
    print("Lista", lista7, "esta ordenada - ", ordenados2)
    lista8 = ["A","B","C"]
    ordenados3 = verListaOrdenada(lista8)
    print("Lista", lista8, "esta ordenada - ", ordenados3)
    lista9 = ["A","Z","K"]
    ordenados4 = verListaOrdenada(lista9)
    print("Lista", lista9, "esta ordenada - ", ordenados4)


    #Anagramas
    print ("")
    print("----------------------------------------------")
    print("EJERCICIO 4: Recibe dos cadenas y devuelve True si es anagrama, False si no lo es")
    print ("")
    p1 = ("amor")
    p2= ("rOmA")
    anagrama= calcularAnagramas(p1,p2)
    print("Las palabras: ",p1,"y",p2,"son anagramas: ", anagrama)
    p3 = ("hola")
    p4= ("ADIos")
    anagrama2= calcularAnagramas(p3,p4)
    print("Las palabras: ",p3,"y",p4,"son anagramas: ", anagrama2)

    #Valor Repetido
    print ("")
    print("----------------------------------------------")
    print("EJERCICIO 5: Recibe una lista, regresa True si algun dato esta duplicado, de lo contrario, regresa False")
    print ("")
    lista10= [1,1,3,4,5]
    repetido= verificarValoresRepetidos(lista10)
    print ("La lista",lista10,"tiene valores repetidos:",repetido)
    lista11= [1,3,4,5]
    repetido2= verificarValoresRepetidos(lista11)
    print("La lista", lista11, "tiene valores repetidos:", repetido2)

    #Borrar valores repetidos, solo dejar 1
    print ("")
    print("----------------------------------------------")
    print("EJERCICIO 6: Recibe una lista y solo deja 1 de los valores repetidos")
    print ("")
    lista12 = [1, 1, 3, 4, 5]
    repetidos = imprimirSoloUnValor(lista12)
    print("La lista:",lista12 ,"sin valores repetidos es:",repetidos)
    lista13 = [1, 3, 4, 5, 1, 1, 2, 3, 3, 4, 4, 6]
    repetidos2 = imprimirSoloUnValor(lista13)
    print("La lista:", lista13 , "sin valores repetidos es:", repetidos2)

main()