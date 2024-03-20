class Conta_Corrente:
    def __init__(self, numero_conta, nome_correntista, saldo):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self):
        self.nome_correntista = str(input("altere o nome do correntista: "))

    def depositar(self, deposito):
        deposito = float(input("Digite o valor do deposito: "))
        self.saldo += deposito 

    def sacar(self, saque):
        saque = float(input("Digite o valor do saque: "))
        self.saldo -= saque

#numero_conta = int(input("Digite o número da conta: "))
#nome_correntista = str(input("Digite o nome do correntista: "))
#saldo = float(input("Digite o saldo da conta: "))
conta = Conta_Corrente(24281, "Flavio", 200)

