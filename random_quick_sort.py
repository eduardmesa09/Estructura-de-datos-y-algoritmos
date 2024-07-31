import random

lista_1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
lista_2 = [46, 38, 6, 40, 5, 45, 8, 19, 48, 37]
lista_3 = [9, 1, 4, 3, 8, 7, 5, 7, 3, 9]
lista_4 = [5, 7, 3, 9, 1, 4, 1, 4, 3, 7]
lista_5 = [6, 2, 8, 5, 4, 9, 1, 6, 8, 2]
lista_6 = [7, 5, 3, 2, 9, 4, 8, 5, 6, 3]
lista_7 = [2, 7, 4, 6, 9, 1, 1, 7, 3, 8]

#Intercambia la posición de dos números dados en una lista.
def swap(index_1, index_2, lista):
    lista[index_1], lista[index_2] = lista[index_2], lista[index_1]

#Dada la posición de un numero inicial (pivote), la posción de un número a comparar (store_index),
#y una lista, envía al pivote a la primera posicíon de las lista usando el método swap, 
#evalua mediante un ciclo for si el pivote es mayor al al isguiente indice en la lista, 
#en caso tal mediante la función swap intercambia dicho indice con la posicíon del store_index
#e incrementa el store_index +1. Al finalizar este ciclo, envía al pivote a la posición del 
#penultimo valor del store_index.
def ordenar(pivote, store_index, lista):
    swap(0, pivote, lista)
    
    for i in range (1, len(lista)):
        if (lista[i] <= lista[0]):
            swap(i, store_index, lista)
            store_index += 1
            
    swap(0, (store_index-1), lista)

#Dada una lista, crea una copia de dicha lista y la organiza usando el método .sort, mediante
#un ciclo while compara si la lista inicial es igual a la lista previamente ordenada, sí no,
# invoca la función ordenar, proporcionando una posición inicial a comparar (1), un pivote al azar
#y una lista. Así hasta que la comparación inicial sea verdadera.
def Random_quick_sort(lista): 
    sorted_list = lista[:]
    sorted_list.sort()
    ciclo= 1
    
    while (lista != sorted_list) :
        pivote = random.randint(0,(len(lista)-1))
        ordenar(pivote, 1, lista)
        print("Ciclo : ", ciclo)
        ciclo+= 1
        print("Resultado :") 
        print(lista)
        print("")
    
Random_quick_sort(lista_2)
