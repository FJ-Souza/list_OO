class Bichinho_virtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self):
        self.nome = str(input("Digite um novo nome: "))

    def alterar_fome(self):
        if self.fome < 100:
            self.fome = int(input("Alterar fome: "))

    def alterar_saude(self):
        if self.saude < 100:
            self.saude = int(input("Alterar valor da saúde: "))
        
    def alterar_idade(self):
        self.idade = int(input("Alterar idade: "))

    def receber_nome(self):
        return self.nome

    def receber_fome(self):
        return self.fome
    
    def receber_saude(self):
        return self.saude
    
    def receber_idade(self):
        return self.idade
    
bichinho = Bichinho_virtual("Totó", 90, 100, 8)
print("Nome: ", bichinho.receber_nome())
print("Fome: ", bichinho.receber_fome())
print("Saúde: ", bichinho.receber_saude())
print("Idade: ", bichinho.receber_idade())

bichinho.alterar_fome()
bichinho.alterar_nome()
bichinho.alterar_saude()
bichinho.alterar_idade()
print("Nome: ", bichinho.receber_nome())
if bichinho.fome > 100:
    print("Não estou com fome")
else:
    print("Fome: ",bichinho.receber_fome())

if bichinho.saude > 100:
    print("Saúde maxima.")
else:
    print("Saúde: ",bichinho.receber_saude())

print("Idade: ", bichinho.receber_idade())