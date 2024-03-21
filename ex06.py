class Tv:
    def __init__(self):
        self.canal_atual = 1
        self.volume = 10

    def mudar_canal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal_atual = novo_canal
            print("Canal alterado para: ", novo_canal)
        else:
            print("Canal inválido.")

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
            print("Volume aumentado para: ", self.volume)
        else:
            print("Volume já esta no máximo.")

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print("Volume diminuido para: ", self.volume)
        else:
            print("Volume já esta no minimo.")

televisor = Tv()
print("Canal atual: ", televisor.canal_atual)
print("Volume atual: ", televisor.volume)

televisor.mudar_canal(50)
televisor.aumentar_volume()
televisor.diminuir_volume()

televisor.mudar_canal(150)
televisor.aumentar_volume()
televisor.diminuir_volume()