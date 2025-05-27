class pessoa:
    def __init__(self, idade=19):
        self.idade = idade
        self.cidade = 'londrina'
        self.solteiro = True
    def pergunta(self, idade):
        print("tenho", int(self.idade), "anos")
        
flavio = pessoa(30)
flavia = pessoa()

flavio.pergunta(10)
