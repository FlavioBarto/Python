#Em uma lista de 15 números com números misturados, substitua os números negativos por zero.

num = [1, 2, -3, 4, -5, 6, -78, 9, 0, 2, 12, -32, 98, -43, -27]

print(num)

for i in range(len(num)): #Percorrer a lista por índice para poder modificar os valores
    if(num[i] < 0): # se a posição que esta com o valor menos de zero vai ser convertida em 0
        num[i] = 0
        

print(num)

