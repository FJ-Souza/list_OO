class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self,valor):
        litrosAbastecidos = valor / self.valorLitro
        if litrosAbastecidos <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litrosAbastecidos
            return litrosAbastecidos
        else:
            return "Não há combustível suficiente na bomba."

    def abastecerPorLitro(self, litros):
        valor_a_pagar = litros * self.valorLitro
        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            return valor_a_pagar
        else:
            return "Não há combustivel suficiente na bomba."

    def alterarValor(self, novoValor):
        self.valorLitro = novoValor

    def alterarCombustivel(self, novoTipo):
        self.tipoCombustivel = novoTipo

    def alterarQuantidadeCombustivel(self, novaQuantidade):
        self.quantidadeCombustivel = novaQuantidade


Bomba = BombaCombustivel("Gasolina", 5.50, 1000)
print("Abastecimento por valor: ")
litros_abastecidos = Bomba.abastecerPorValor(55)
print("Litros abastecido: ", litros_abastecidos)
print("Quantidade de combustivel restante na bomba: ", Bomba.quantidadeCombustivel)

print("\nAbastecendo por litro: ")
valor_a_pagar = Bomba.abastecerPorLitro(20)
print("valor a pagar: ", valor_a_pagar)
print("Quantidade de combustivel restante na bomba: ", Bomba.quantidadeCombustivel)

print("\nAlterando o valor do litro de combustível:")
Bomba.valorLitro = 5.80
print("Novo valor do litro de combustível:", Bomba.valorLitro)

print("\nAlterando o tipo de combustível:")
Bomba.tipoCombustivel = "Álcool"
print("Novo tipo de combustível:", Bomba.tipoCombustivel)

print("\nAlterando a quantidade de combustível na bomba:")
Bomba.quantidadeCombustivel = 900
print("Nova quantidade de combustível na bomba:", Bomba.quantidadeCombustivel)