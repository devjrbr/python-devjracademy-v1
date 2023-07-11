# Heranca


class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome: str = nome
        self.idade: str = idade

    def falar(self):
        print(f"{self.nome} está falando...")


class Cliente(Pessoa):
    carrinho = []

    def __init__(self, nome, idade, carrinho) -> None:
        super().__init__(nome, idade)

        self.carrinho = carrinho


class Carro(Cliente):
    tipo: str = "Sedan"
    
    def __init__(self, nome, idade, carrinho, tipo) -> None:
        super().__init__(nome, idade, carrinho)

        self.tipo = tipo



c1 = Cliente("Maria", 30, ["Mouse", "Teclado"])
c2 = Cliente("João", 20, ["Monitor", "Gabinete"])
c3 = Cliente("Pedro", 25, ["SSD", "HDD"])

carro1 = Carro("Fiat", 2020, ["Volante", "Retrovisor"], "Sedan")
carro2 = Carro("Ferrari", 2021, ["Volante", "Retrovisor"], "Esportivo")
carro3 = Carro("BMW", 2022, ["Volante", "Retrovisor"], "Sedan")


for p in [c1, c2, c3]:
    p.falar()
