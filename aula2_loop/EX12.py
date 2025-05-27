#Percorra uma lista de 1 a 50000 e Some todos os números dela usando um loop.
lista = []
soma = 0
for i in range(50001):
    lista.append(i)

for i in range(len(lista)):
    soma += lista[i]

print(soma)