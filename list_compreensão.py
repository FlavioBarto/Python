lista= [1, 2, 3, 4, 5]
lista_duplicada= [ 2 * item for item in lista]

print(lista)
print(lista_duplicada)

#----------------------------------------
lista100 = list(range(100))

listadiv20 = [item for item in lista100 if item % 20 == 0]

print(lista100)
print(listadiv20)
#----------------------------------------
texto = 'why did, you want, to meet, with me'
lista_texto = texto.split(',')
print(lista_texto)

def limpa(palavra):
    return palavra.replace(',', '').lower()


palavra_texto = [limpa(palavra) for palavra in texto.split(',')]
print(palavra_texto)
#print(limpa(texto))