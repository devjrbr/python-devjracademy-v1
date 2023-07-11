class Pessoa:
    peso: float = 0.0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def definir_peso(self, peso):
        self.peso = peso

    def pegar_peso(self):
        return self.peso

    def falar(self):
        print(f"{self.nome} está falando...")


p1 = Pessoa(nome="Nicolas", idade=23)
p2 = Pessoa(nome="Sofia", idade=18)
p3 = Pessoa(nome="Nephi", idade=21)


todas_as_pessoas = [p1, p2, p3]

for p in todas_as_pessoas:
    p.falar()
