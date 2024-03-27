class Macaco:
    def _init_(self, nome):
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


# Criando dois macacos
macaco1 = Macaco("Macaco 1")
macaco2 = Macaco("Macaco 2")

# Alimentando os macacos
macaco1.comer("banana")
macaco2.comer("maçã")
macaco1.comer("laranja")

# Verificando o conteúdo do estômago
macaco1.verBucho()
macaco2.verBucho()

# Digerindo
macaco1.digerir()
macaco2.digerir()

# Verificando novamente o conteúdo do estômago após a digestão
macaco1.verBucho()
macaco2.verBucho()

# Experimento: fazendo um macaco comer o outro
macaco2.comer("Macaco 1")

# Verificando o conteúdo do estômago após o experimento
macaco2.verBucho()