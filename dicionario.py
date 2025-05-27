from collections import defaultdict


pedidos = [
    ('Ana',    'camisa'),
    ('Bruno',  'calça'),
    ('Ana',    'boné'),
    ('Ana',    'chinelo'),
    ('Ana',    'vestido'),
    ('Bruno',    'camisa')
]


agrupado = defaultdict(list)


for cliente, produto in pedidos:
    agrupado[cliente].append(produto)


print(dict(agrupado))
print(agrupado)
# {'Ana': ['camisa', 'boné'], 'Bruno': ['calça']}