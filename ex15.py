class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.tedio = 50

    def alimentar(self, quantidade):
        self.fome -= quantidade

    def brincar(self, tempo):
        self.tedio -= tempo

    def humor(self):
        if self.fome <= 30 and self.tedio <= 30:
            return "Feliz"
        elif self.fome > 70:
            return "Faminto"
        elif self.tedio > 70:
            return "Entediado"
        else:
            return "Normal"


nome_bichinho = input("Qual o nome do seu bichinho virtual? ")
bichinho = BichinhoVirtual(nome_bichinho)

print(f"{bichinho.nome} está {bichinho.humor()}.")

comida = int(input("Quantidade de comida fornecida (0-50): "))
tempo_brincadeira = int(input("Tempo de brincadeira (0-50): "))

bichinho.alimentar(comida)
bichinho.brincar(tempo_brincadeira)

print(f"{bichinho.nome} está {bichinho.humor()} depois de comer e brincar.")