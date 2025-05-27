#Crie uma nova lista apenas com os elementos maiores que 50 de uma lista original.
lista = []
lista50 = []

for i in range(100):
    lista.append(i)

for i in range(len(lista)):
    if (lista[i]>=50):
        lista50.append(lista[i])

print(lista50)