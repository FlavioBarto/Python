#Leia uma linha do usuário contendo palavras separadas por espaço, aplique split(), use reverse() na lista, e então join("-") para mostrar as palavras invertidas.

linha = input("mande uma mensagem: ")

linha = linha.split(" ")
print(linha)
linha.reverse()
print(linha)
linha = ("-").join(linha)
print(linha)