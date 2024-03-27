class Carro:
    def _init_(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def andar(self, distancia):
        combustivel_necessario = distancia / self.consumo
        if combustivel_necessario <= self.combustivel:
            self.combustivel -= combustivel_necessario
            print(f"O carro percorreu {distancia} quilômetros.")
        else:
            print("Não há combustível suficiente para percorrer essa distância.")

    def obterGasolina(self):
        print(f"Nível atual de combustível: {self.combustivel} litros.")

    def adicionarGasolina(self, quantidade):
        self.combustivel += quantidade
        print(f"Foram adicionados {quantidade} litros de combustível.")


meuFusca = Carro(15)
meuFusca.adicionarGasolina(20)
meuFusca.andar(100)
meuFusca.obterGasolina()