#Crie uma lista com 10 valores e gere uma nova lista contendo o quadrado de cada número (use loop + .append()).
lista = []
for i in range(11):
    lista.append(i)
print(lista)
listaQuadrada = []
for i in range(len(lista)):
    listaQuadrada.append(lista[i] ** 2)

print(listaQuadrada)