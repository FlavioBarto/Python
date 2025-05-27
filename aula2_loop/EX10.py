#Substitua todos os elementos de uma lista de strings que comecem com a letra "a" por "***". [aranha, banana, agua, butina, cachorro, anel,aliança,cabrito,zebra,cola,azul,amarelo,roxo,rosa]
lista = ["aranha", "banana", "agua", "butina", "cachorro", "anel", "aliança", "cabrito", "zebra", "cola", "azul", "amarelo", "roxo", "rosa"]
nova_lista = [item if not item.startswith("a") else "***" for item in lista] # Substitui elementos que começam com "a" por "***"
print(nova_lista)
