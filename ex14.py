class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

    def aumentarSalario(self, porcentagemDeAumento):
        aumento = self.salario * (porcentagemDeAumento / 100)
        self.salario += aumento


funcionario1 = Funcionario("João", 2500.00)
funcionario2 = Funcionario("Maria", 3000.00)

print("Salário do funcionário 1 antes do aumento:", funcionario1.getSalario())
print("Salário do funcionário 2 antes do aumento:", funcionario2.getSalario())

funcionario1.aumentarSalario(10)
funcionario2.aumentarSalario(10)

print("Salário do funcionário 1 após o aumento:", funcionario1.getSalario())
print("Salário do funcionário 2 após o aumento:", funcionario2.getSalario())