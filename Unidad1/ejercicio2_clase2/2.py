import time
inicio = time.time()

def potencia(base, exponente):
    potencia = 1
    for i in range(1, exponente+1):
        potencia = potencia * base

    print(potencia)

potencia(1,0)

fin = time.time()
print(fin-inicio)