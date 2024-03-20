class Bola:
    def __init__(self, cor, circunferencia,material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostrarCor(self):
        return self.cor
    
bola = Bola("azul", 10, "couro")
print("Cor da bola: ", bola.mostrarCor())
bola.trocaCor("Vermelho")
print("Nova cor da bola: ", bola.mostrarCor())