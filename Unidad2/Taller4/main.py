import random
import time

def crear_lista(cantidad):
    lista = []
    while len(lista) <= cantidad:
        dato = random.randint(1,100000000000)
        if not (dato in lista):
            lista.append(dato)
    return lista

def burbuja(lista):
    for i in range(0, len(lista) - 1):
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux



def burbujaMejorada(lista):
    i = 0
    control = True
    while (i <= len(lista) - 2) and control:
        control = False
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
                control = True
        i = i + 1


def burbujaBidireccional(lista):
    izquierda = 0
    derecha = len(lista) - 1
    control = True
    while (izquierda < derecha) and control:
        control = False
        for i in range(izquierda, derecha):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                control = True
        derecha -= 1
        for j in range(derecha, izquierda, -1):
            if lista[j] < lista[j - 1]:
                aux = lista[j]
                lista[j] = lista[j - 1]
                lista[i - 1] = aux
                control = True
        izquierda += 1


def seleccion(lista):
    for i in range(0, len(lista) - 1):
        minimo = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j
        aux = lista[i]
        lista[i] = lista[minimo]
        lista[minimo] = aux


def insercion(lista):
    for i in range(1, len(lista) + 1):
        k = i - 1
        while (k > 0) and lista[k] < lista[k - 1]:
            aux = lista[k]
            lista[k] = lista[k - 1]
            lista[k - 1] = aux
            k -= 1


def ordenamientoRapido(lista, primero, ultimo):
    izquierda = primero
    derecha = ultimo - 1
    pivote = ultimo
    while izquierda < derecha:
        while lista[izquierda] < lista[pivote] and izquierda <= derecha:
            izquierda += 1
        while lista[derecha] > lista[pivote] and derecha >= izquierda:
            derecha -= 1
        if izquierda < derecha:
            aux = lista[izquierda]
            lista[izquierda] = lista[derecha]
            lista[derecha] = aux
    if lista[pivote] < lista[izquierda]:
        aux = lista[izquierda]
        lista[izquierda] = lista[pivote]
        lista[pivote] = aux
    if primero < izquierda:
        ordenamientoRapido(lista, primero, izquierda - 1)
    if ultimo > izquierda:
        ordenamientoRapido(lista, izquierda + 1, ultimo)


def ordenamientoMezcla(lista):
    if len(lista) <= 1:
        return lista
    else:
        medio = len(lista) // 2
        izquierda = []
        for i in range(0, medio):
            izquierda.append(lista[i])
        derecha = []
        for i in range(medio, len(lista)):
            derecha.append(lista[i])
        izquierda = ordenamientoMezcla(izquierda)
        derecha = ordenamientoMezcla(derecha)
        if izquierda[medio - 1] <= derecha[0]:
            izquierda += derecha
            return izquierda
        resultado = mezcla(izquierda, derecha)
        return resultado


def mezcla(izquierda, derecha):
    lista_mezclada = []
    while len(izquierda)>0 and (len(derecha) > 0):
        if izquierda[0] < derecha[0]:
            lista_mezclada.append(izquierda.pop(0))
        else:
            lista_mezclada.append(derecha.pop(0))
    if len(izquierda) > 0:
        lista_mezclada += izquierda
    if len(derecha) > 0:
        lista_mezclada += derecha
    return lista_mezclada

class nodoArbol(object):
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info

def insertarNodo(raiz, info):
    if(raiz is None):
        raiz = nodoArbol(info)
    elif(info < raiz.info):
        raiz.izq = insertarNodo(raiz.izq,info)
    else:
        raiz.der = insertarNodo(raiz.der,info)
    return raiz

def crearArbol(lista):
    raiz = None
    for i in lista:
        raiz = insertarNodo(raiz, i)
    return raiz
    

if __name__ == "__main__":
    lista = crear_lista(1000000)
    
    """inicio = time.time()
    burbuja(lista)
    fin = time.time()
    tiempo = fin-inicio

    inicio = time.time()
    burbujaMejorada(lista)
    fin = time.time()
    tiempo = fin-inicio

    inicio = time.time()
    burbujaBidireccional(lista)
    fin = time.time()
    tiempo = fin-inicio

    inicio = time.time()
    seleccion(lista)
    fin = time.time()
    tiempo = fin-inicio

    inicio = time.time()
    insercion(lista)
    fin = time.time()
    tiempo = fin-inicio

    inicio = time.time()
    ordenamientoRapido(lista,0,len(lista)-1)
    fin = time.time()
    tiempo = fin-inicio

    inicio = time.time()
    ordenamientoMezcla(lista)
    fin = time.time()
    tiempo = fin-inicio"""

    inicio = time.time()
    crearArbol(lista)
    fin = time.time()
    tiempo = fin-inicio

    print(tiempo)
