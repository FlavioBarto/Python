
nomeArquivo = "Frutas.txt"
frutas = []
with open(nomeArquivo, "r") as arquivo:
    for linha in arquivo:
        fruta = linha.strip()
        if fruta:
            frutas.append(fruta)
        
frutas_ordenadas = sorted(frutas)

frutas.count(frutas)
print(sorted(frutas))