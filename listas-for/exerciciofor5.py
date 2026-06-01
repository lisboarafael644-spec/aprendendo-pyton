senhaCorreta = "1234"

for tentativa in range(3):
    senha = input("Digite a senha: ")

    if senha == senhaCorreta:
        print("Acesso Permitido")
        break

    else:
        print("Senha incorreta")

if senha != senhaCorreta:
    print("Conta Bloqueada")