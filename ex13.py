class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario


funcionario1 = Funcionario("João", 2500.00)
funcionario2 = Funcionario("Maria", 3000.00)

print("Nome do funcionário 1:", funcionario1.getNome())
print("Salário do funcionário 1:", funcionario1.getSalario())

print("Nome do funcionário 2:", funcionario2.getNome())
print("Salário do funcionário 2:", funcionario2.getSalario())