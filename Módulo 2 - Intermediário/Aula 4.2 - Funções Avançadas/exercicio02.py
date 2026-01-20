def print_cadastro(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

def get_cadastro():
    cadastros = []

    while True:
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        email = input("Digite seu email: ")

        cadastros.append({
            "nome": nome,
            "idade": idade,
            "email": email
        })

        continuar = input("Cadastrar novo usuário? (s/n): ").lower()
        if continuar != "s":
            break

    print("=== CADASTROS ===")
    for cadastro in cadastros:
        print_cadastro(**cadastro)
        print("-" * 20)

get_cadastro()