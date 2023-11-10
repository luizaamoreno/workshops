users = []

def addUser(user, password):
    usuario = {
        'usuario': user,
        'senha': password
    }

    if len(user) >= 3:
        print("usuário cadastrado com sucesso!")
        users.append(usuario)
        return True
    else:
        print("Digite um nome de usuário com pelo menos 3 caracteres.")

def login(user, password):
    for usuario in users:
        if usuario['usuario'] == user and usuario['senha'] == password:
            print("Seja bem-vindo! Login realizado com sucesso!")
        else:
            print("Usuário ou senha incorretos.")

while True:
    op = input(""" 
                [1] - Cadastrar novo usuário
                [2] - Entrar
                [3] - Sair
                
                Digite a opção desejada: """)
    
    if op == "1":
        nome = input("usuário: ").strip()
        senha = input("senha: ").strip()
        addUser(nome, senha)

    elif op == "2":
        nome = input("usuário: ").strip()
        senha = input("senha: ").strip()
        login(nome, senha)

    elif op == "3":
        print("Até a próxima.")
        break

    else:
        print("Você digitou uma entrada inválida. Selecione uma opção válida.")
        