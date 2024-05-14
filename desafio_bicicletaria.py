class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando a bicicleta...")
        print("Bicicleta parada !")

    def correr(self):
        print("Vrummmmm...")

    # def trocar_marcha(self, num_marcha):
    #     print("Trocando marcha...")
    #     _self = self
    #
    #     def _trocar_marcha():
    #         if num_marcha > _self.marcha:
    #             print("Marcha trocada...")
    #         else:
    #             print("Nã foi possível trocar de marcha...")

#    def __str__(self):
#        return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
#        return f"{self.__class__.__name__}: {[f'{chave} = {valor}' for chave, valor in self.__dict__.items()]}"

#    def get_cor(self):
#        return self.cor


b1 = Bicicleta("Vermelha", "Caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("Verde", "Monark", 2000, 189)
#Bicicleta.buzinar() # Error
#Bicicleta.buzinar(b2)
#print(b2.get_cor())
b2.buzinar()

b2.trocar_marcha()
#print(b2)

