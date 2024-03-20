class Pessoa:

    def __init__(self,nome:str,idade:int,peso:float,altura:float):
        self.nome = nome
        self._idade = idade
        self.__peso = peso
        self.altura = altura
    
    def envelhecer(self):
        self._idade += 1
        self.crescer()

    def crescer(self):
        if self._idade < 21:
            self.altura += 0.05
        elif self._idade < 50 and self._idade > 21:
            self._idade += 0.01
        else:
            self.altura -= 0.01    

    def engordar(self, grama:float):
        self.__peso += grama

    def emagrecer(self, grama:float):
        self.__peso -= grama

    def __str__(self):
        return f"Eu sou o {self.nome} tenho {self._idade} com {self.__peso}Kg e {self.altura}M."

    def peso(self)->float:
        return self.__peso

flavio = Pessoa("Flavio Júnior",19,80.120,1.80)     
print(flavio)  

glaucia = Pessoa("Glaucia Cristina",19,90.400,1.90)  
print(glaucia)