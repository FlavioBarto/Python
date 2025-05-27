#Dada a lista ['banana', 'maçã', 'banana', 'laranja'], substitua todas as ocorrências de "banana" por "abacaxi".
lista = ['banana', 'maçã', 'banana', 'laranja']
print(lista)
for i in range(len(lista)):
    if(lista[i] == 'banana'):
        lista[i] = 'abacaxi'

print(lista)
