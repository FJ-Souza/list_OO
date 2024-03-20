class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def novo_valor(self):
        self.base = int(input("Digite uma nova base: "))
        self.altura = int(input("Digite uma nova altura: "))

    def mostrar_valor(self):
        print(f"Base: {self.base} e Altura: {self.altura}")

    def calcular(self):
        print("Área do retangulo: ", self.base * self.altura)
        print("Perimetro do retangulo: ", 2 * (self.base + self.altura))

retangulo = Retangulo(8, 12)
retangulo.mostrar_valor()
retangulo.calcular()
retangulo.novo_valor()
retangulo.mostrar_valor()
retangulo.calcular()
