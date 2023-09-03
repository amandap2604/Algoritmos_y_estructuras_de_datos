import time
inicio = time.time()

def factorial(numero):
    resultado = 1
    for i in range(1, numero+1):
        resultado = resultado * i
    print(resultado)

factorial(0)
fin = time.time()
print(fin-inicio)