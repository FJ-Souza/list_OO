class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)
        print(f"{self.nome} comeu {alimento}.")

    def verBucho(self):
        if self.bucho:
            print(f"{self.nome} tem no estômago: {', '.join(self.bucho)}.")
        else:
            print(f"{self.nome} está com o estômago vazio.")

    def digerir(self):
        if self.bucho:
            print(f"{self.nome} está digerindo...")
            self.bucho = []
        else:
            print(f"{self.nome} não tem nada para digerir.")


macaco1 = Macaco("Macaco 1")
macaco2 = Macaco("Macaco 2")

macaco1.comer("banana")
macaco2.comer("maçã")
macaco1.comer("laranja")

macaco1.verBucho()
macaco2.verBucho()

macaco1.digerir()
macaco2.digerir()

macaco1.verBucho()
macaco2.verBucho()

macaco2.comer("Macaco 1")

macaco2.verBucho()