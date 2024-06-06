class Cachorro:

    def __init__(self, nome, cor, acordado=True):
        print("Iniciando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado


    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("au au")

def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


#c = Cachorro("Chappie", "amarelo")
#c.falar()

criar_cachorro()