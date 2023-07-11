# Polimorfismo

# Polimorfismo é o princípio pelo qual duas ou mais classes derivadas
# de uma mesma superclasse podem invocar métodos que têm a mesma assinatura mas
# comportamentos distintos.
# superclasse é a classe que é herdada, subclasse é a classe que herda.


# Classe base
class Animal:
    def fazer_barulho(self):
        print("O animal faz barulho.")


# Subclasse 1
class Cachorro(Animal):
    def fazer_barulho(self):
        print("O cachorro late.")


# Subclasse 2
class Gato(Animal):
    def fazer_barulho(self):
        print("O gato mia.")


# Criando instâncias das classes
animal0 = Animal()
animal1 = Cachorro()
animal2 = Gato()

# Chamando o método fazer_barulho()
animal0.fazer_barulho()
animal1.fazer_barulho()
animal2.fazer_barulho()


class LerArquivo:
    def ler(self):
        print("Lendo arquivo...")

    def remover(self):
        print("Removendo arquivo...")


class LerAquivoJson(LerArquivo):
    def ler(self):
        arquivo = open("arquivo.json", "r")
        arquivo.read()

    def remover(self):
        import os

        os.remove("arquivo.json")


class LerArquivoCSV(LerArquivo):
    def ler(self):
        print("Iniciando")
        arquivo = open("arquivo.json", "r")
        arquivo.read()
        print("Finalizando")

    def remover(self):
        import os

        os.remove("arquivo.json")
