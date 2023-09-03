import time
inicio = time.time()
def suma_consecutiva(numero):
    suma = 0
    for i in range(1, numero+1):
        suma += i
    print(suma)

suma_consecutiva(100)
fin = time.time()
print(fin-inicio)
