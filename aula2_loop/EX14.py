#Concatene "Olá " com cada nome de uma lista, formando uma nova saudação para cada pessoa. (EX: Olá, João. Olá, Ana)
lista = ['nome', 'nome', 'nome', 'nome', 'nome', 'nome', 'nome', 'nome', 'nome', 'nome', 'nome', 'nome', 'nome', 'nome', 'nome']
for i in range(len(lista)):
    lista[i] = 'Ola, ' + lista[i]
print(lista)