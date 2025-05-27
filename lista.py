#a = range(1, 10) #desse jeito não tem como aumentar ou diminuir pq não é uma lista
a = list(range(1, 10)) #agora sim se torna uma lista por causa do list
print((a))

a.append(11)
print(list(a))