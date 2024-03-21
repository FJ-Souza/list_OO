class Bichinho_virtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self):
        self.nome = str(input("Digite nome: "))

    def comer(self):
        self.fome = 