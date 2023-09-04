import sys
inicio = time.time()
sys.setrecursionlimit(10 ** 9)
def factorial_recursivamente(numero):
    if numero == 1 or numero == 0:
        return 1
    else:
        return numero * factorial_recursivamente(numero-1)

print(factorial_recursivamente(10000))
fin = time.time()
print(fin-inicio)
