itens = [19, 'flavio', 1.15, True, 'gustavo', 12, 100.15, True, 'gabriel', 'tipo']
print(itens)

itens.append(100)
print(itens)

if(itens.__contains__(100)):
    itens.remove(100)
else:
    print("não existe na lista")

print(itens)