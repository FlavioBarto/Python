lista = ['floresta', 'riacho', 'arvores']

dicionario = {f'{len(item)} - {item[0]}': item for item in lista} #pega o comprimento do item e seu primeiro numero, o item vem do for seria cada valor na lista
print(dicionario)
x, y = ('ceu', 'cinza')
print(y)
tupla = [('ceu', 'azul')]

for a, b in tupla:
    print(f'{a} --- {b}')
#-----------------------------------------
lista_tuplas = [('ceu', 'cinza'), ('corredor', 'escuro'), ('chão', 'molhado')]

dicionario_tuplas = {chave: valor for (chave, valor) in lista_tuplas} 

print(dicionario_tuplas)

dicionario_modificado = {chave: (valor * 2) for (chave, valor) in dicionario_tuplas.items()} 
print(dicionario_modificado)
dicionario_modificado2 = {chave: valor for (chave, valor) in dicionario_tuplas.items() if len(chave) <= 5} 
print(dicionario_modificado2)