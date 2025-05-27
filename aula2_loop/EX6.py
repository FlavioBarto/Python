#Remova todos os elementos "None" de uma lista, substituindo-os por "Indefinido". [12,58,46,None,69,47,None,None,None,100]
lista = [12,58,46,None,69,47,None,None,None,100]
print(lista)
for i in range(len(lista)):
    if(lista[i] == None):
        lista[i] = "Indefinido"

print(lista)