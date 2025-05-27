from collections import defaultdict

dicionario = {
    'nome': 'flavio',
    'idade': 19,
    'cidade': 'londrina'
}

print(dicionario.keys())
print(list(dicionario.keys()))
print(dicionario.values())
print(list(dicionario.values()))

print(dicionario['nome'])
print(dicionario['cidade'])
dicionario['cidade'] = 'lisboa'
print(dicionario['cidade'])
dicionario['solteiro'] = 'sim'
print(dicionario['solteiro'])
print(dicionario)

#------------------------------------

dicionario['organiza'] = ['reunião', 'kambam', 'RH']
dicionario['organiza'].append('pasta')
print(dicionario)
#------------------------------------

natureza = defaultdict(list)
print(natureza)
natureza['fauna'].extend(['papagaio', 'cachorro', 'gato'])
print(natureza)
print(natureza['fauna'][2])