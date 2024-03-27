class BichinhoVirtual:
    def _init_(self, nome):
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

    def _str_(self):
        return f"Bichinho {self.nome}: fome={self.fome}, tédio={self.tedio}"


nome_bichinho = input("Qual o nome do seu bichinho virtual? ")
bichinho = BichinhoVirtual(nome_bichinho)

while True:
    print("\n1. Alimentar bichinho")
    print("2. Brincar com bichinho")
    print("3. Mostrar humor do bichinho")
    print("4. Opção secreta (mostrar valores exatos dos atributos)")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        comida = int(input("Quantidade de comida fornecida (0-50): "))
        bichinho.alimentar(comida)
    elif escolha == "2":
        tempo_brincadeira = int(input("Tempo de brincadeira (0-50): "))
        bichinho.brincar(tempo_brincadeira)
    elif escolha == "3":
        print(f"{bichinho.nome} está {bichinho.humor()}.")
    elif escolha == "4":
        print(bichinho)
    elif escolha == "5":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")