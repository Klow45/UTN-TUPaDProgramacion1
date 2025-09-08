## Ejercicio 6
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

from statistics import mode, median, mean

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print("Modo:", moda)
print("Mediana:", mediana)
print("Media:", media)

# Determina el tipo de sesgo
if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha.")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda.")
elif media == mediana == moda:
    print("Sin sesgo: media, mediana y moda son iguales.")
else:
    print("No hay un sesgo claro.")
