import random

lista_1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
lista_2 = [46, 38, 6, 40, 5, 45, 8, 19, 48, 37]
lista_3 = [9, 1, 4, 3, 8, 7, 5, 7, 3, 9]
lista_4 = [5, 7, 3, 9, 1, 4, 1, 4, 3, 7]
lista_5 = [6, 2, 8, 5, 4, 9, 1, 6, 8, 2]
lista_6 = [7, 5, 3, 2, 9, 4, 8, 5, 6, 3]
lista_7 = [2, 7, 4, 6, 9, 1, 1, 7, 3, 8]

def swap(index_1, index_2, lista):
    lista[index_1], lista[index_2] = lista[index_2], lista[index_1]

def evaluate(pivote, store_index, lista):
    swap(0, pivote, lista)
    for i in range (1, len(lista)):
        if (lista[i] <= lista[0]):
            swap(i, store_index, lista)
            store_index += 1
    swap(0, (store_index-1), lista)
    return store_index

def Random_quick_sort(lista): 
    sorted_list = lista[:]
    sorted_list.sort()
    
    while (lista != sorted_list) :
        pivote = random.randint(0,(len(lista)-1))
        store_index = 1
        evaluate(pivote, store_index, lista)
        print(lista)
    
Random_quick_sort(lista_1)