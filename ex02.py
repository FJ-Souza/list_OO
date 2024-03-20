class Quadrado:
    def __init__(self, tamanhoLado):
        self.tamanhoLado = tamanhoLado

    def trocaTamanho(self):
        self.tamanhoLado = int(input("Digite um novo tamanho: "))

    def mostrarTamanho(self):
        return self.tamanhoLado
    
    def calcular(self):
        return self.tamanhoLado * self.tamanhoLado
    

quadrado = Quadrado(2)
print("Tamanho do lado do quadrado: ", quadrado.mostrarTamanho())
print("Tamanho da Área: ", quadrado.calcular())
quadrado.trocaTamanho()
print("Tamanho do lado do quadrado: ", quadrado.mostrarTamanho())
print("Tamanho da Área: ", quadrado.calcular())