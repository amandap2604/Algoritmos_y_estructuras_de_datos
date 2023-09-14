import time
import random

def promedio_notas(cantidad_asignaturas):
    cantidad_notas = 13
    suma_promedios_asignaturas = 0
    for i in range(cantidad_asignaturas):
        suma_notas = 0
        for j in range(cantidad_notas):
            nota_obtenida = random.randint(1,7)
            suma_notas += nota_obtenida
            if j == (cantidad_notas - 1):
                suma_promedios_asignaturas += (suma_notas / cantidad_notas)
    promedio_general = suma_promedios_asignaturas / cantidad_asignaturas
    return promedio_general

if __name__ == "__main__":
    inicio = time.time()
    #Varía solo en la cantidad de asignaturas.
    print(promedio_notas(100))
    fin = time.time()
    print(fin-inicio)
