# Exemplo de laço for que itera sobre uma lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

# Exemplo de laço for com range()
for i in range(1, 5):
    print(i)

# Exemplo de laço while que imprime números de 1 a 5
i = 1
while i <= 5:
    print(i)
    i += 1

# Exemplo de laço while com condição de saída
senha_correta = "senha123"
tentativa = input("Digite a senha: ")
while tentativa != senha_correta:
    print("Senha incorreta. Tente novamente.")
    tentativa = input("Digite a senha: ")
print("Acesso concedido!")


# Exemplo de laço do-while que solicita um número até ser digitado um valor maior que 10
while True:
    numero = int(input("Digite um número: "))
    if numero > 10:
        break

