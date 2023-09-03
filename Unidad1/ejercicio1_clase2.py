import time
inicio = time.time()
def numeros_pares_impares(numero):
    cont_imp = 0
    for i in range(1, numero+1):
        if (i%2 == 0):
            print(i, 'Es par')
        else:
            print(i, 'Es impar')
            cont_imp += 1
    print('Cantidad de números impares:', cont_imp)


numeros_pares_impares(100000)
fin = time.time()
print(fin-inicio)