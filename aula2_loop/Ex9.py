#Leia uma frase, quebre com split() e transforme todas as palavras com mais de 5 letras em "LONGA".

frase = input("me mostre uma frase: ")

frase = frase.split()

for i in range(len(frase)):
    if(len(frase[i]) > 5):
        frase[i] = "LONGA"

print(frase)
