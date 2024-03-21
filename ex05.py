class Conta_Corrente:
    def __init__(self, numero_conta, nome_correntista, saldo):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self):
        self.nome_correntista = str(input("altere o nome do correntista: "))

    def retornar_nome(self):
        return self.nome_correntista

    def depositar(self):
        deposito = float(input("Digite o valor do deposito: "))
        self.saldo += deposito 

    def sacar(self):
        saque = float(input("Digite o valor do saque: "))
        self.saldo -= saque

    def retornar_saldo(self):
        return self.saldo
#numero_conta = int(input("Digite o número da conta: "))
#nome_correntista = str(input("Digite o nome do correntista: "))
#saldo = float(input("Digite o saldo da conta: "))

conta = Conta_Corrente(24281, "Flavio", 200)
print("Nome do correntista: ", conta.retornar_nome())
print("Saldo da conta: ", conta.retornar_saldo())
conta.alterar_nome()
print("Nome alterado para: ", conta.retornar_nome())
conta.depositar()
print("Saldo pós deposito: R$", conta.retornar_saldo())
conta.sacar()
print("Saldo pós saque: R$", conta.retornar_saldo())