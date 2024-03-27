import random

class BichinhoVirtual:
    def _init_(self, nome):
        self.nome = nome
        self.fome = random.randint(1, 100)
        self.tedio = random.randint(1, 100)

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

    def _str_(self):
        return f"Bichinho {self.nome}: fome={self.fome}, tédio={self.tedio}"


class FazendaDeBichinhos:
    def _init_(self):
        self.bichinhos = []

    def adicionar_bichinho(self, bichinho):
        self.bichinhos.append(bichinho)

    def alimentar_todos(self, quantidade):
        for bichinho in self.bichinhos:
            bichinho.alimentar(quantidade)

    def brincar_com_todos(self, tempo):
        for bichinho in self.bichinhos:
            bichinho.brincar(tempo)

    def ouvir_todos(self):
        for bichinho in self.bichinhos:
            print(f"{bichinho.nome} está {bichinho.humor()}.")

    def _str_(self):
        return '\n'.join(str(bichinho) for bichinho in self.bichinhos)


fazenda = FazendaDeBichinhos()

fazenda.adicionar_bichinho(BichinhoVirtual("Bichinho1"))
fazenda.adicionar_bichinho(BichinhoVirtual("Bichinho2"))
fazenda.adicionar_bichinho(BichinhoVirtual("Bichinho3"))

while True:
    print("\n1. Alimentar todos os bichinhos")
    print("2. Brincar com todos os bichinhos")
    print("3. Ouvir todos os bichinhos")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        comida = int(input("Quantidade de comida fornecida (0-50): "))
        fazenda.alimentar_todos(comida)
    elif escolha == "2":
        tempo_brincadeira = int(input("Tempo de brincadeira (0-50): "))
        fazenda.brincar_com_todos(tempo_brincadeira)
    elif escolha == "3":
        fazenda.ouvir_todos()
    elif escolha == "4":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

    print("Situação da Fazenda de Bichinhos:")
    print(fazenda)