#Dada uma lista com strings, adicione o sufixo "@gmail.com" em cada item.
lista = ['nome', 'nome', 'nome', 'nome', 'nome', 'nome', 'nome', 'nome', 'nome', 'nome', 'nome', 'nome', 'nome', 'nome', 'nome']


email_completo = [nome + "@gmail.com" for nome in lista]

print(email_completo)

#ou pode ser feito:

emails = ['ana', 'bruno', 'carla', 'daniel']
emails_completos = []

for nome in emails:
    emails_completos.append(nome + "@gmail.com")

print(emails_completos)
    