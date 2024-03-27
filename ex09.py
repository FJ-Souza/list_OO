class Ponto:
    def _init_(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Ponto: ({self.x}, {self.y})")


class Retangulo:
    def _init_(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self):
        x_centro = self.ponto_inicial.x + self.largura / 2
        y_centro = self.ponto_inicial.y + self.altura / 2
        return Ponto(x_centro, y_centro)


def imprimir_centro(retangulo):
    centro = retangulo.encontrar_centro()
    print("Centro do Retângulo:")
    centro.imprimir()


def alterar_retangulo(retangulo):
    novo_x = float(input("Novo valor de x para o ponto inicial do retângulo: "))
    novo_y = float(input("Novo valor de y para o ponto inicial do retângulo: "))
    nova_largura = float(input("Nova largura do retângulo: "))
    nova_altura = float(input("Nova altura do retângulo: "))
    retangulo.ponto_inicial.x = novo_x
    retangulo.ponto_inicial.y = novo_y
    retangulo.largura = nova_largura
    retangulo.altura = nova_altura
    print("Valores do retângulo alterados com sucesso.")


ponto_inicial = Ponto(0, 0)
retangulo = Retangulo(ponto_inicial, 5, 3)

while True:
    print("\n1. Imprimir centro do retângulo")
    print("2. Alterar valores do retângulo")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        imprimir_centro(retangulo)
    elif opcao == "2":
        alterar_retangulo(retangulo)
    elif opcao == "3":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")