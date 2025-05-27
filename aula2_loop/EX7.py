#Percorra uma lista de 1 a 50000 e conte quantos números pares existem nela (use um contador).
contador = 0
lista = []
for i in range(50000):
    lista.append(i)

print(lista)

for i in range(len(lista)):
    if(lista[i] % 2 == 0):
        contador = contador + 1

print(contador)