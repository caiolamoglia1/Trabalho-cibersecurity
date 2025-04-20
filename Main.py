import json

# Simula um arquivo de texto na memória
arquivo_simulado = ""

# Carrega usuários
with open('usuarios.json', 'r') as file:
    usuarios = json.load(file)

# Carrega permissões
try:
    with open('permissoes.json', 'r') as file:
        permissoes = json.load(file)
except FileNotFoundError:
    permissoes = {}

def salvar_usuarios():
    with open('usuarios.json', 'w') as file:
        json.dump(usuarios, file, indent=4)

def salvar_permissoes():
    with open('permissoes.json', 'w') as file:
        json.dump(permissoes, file, indent=4)

def cadastrar():
    print("\n--- Cadastro ---")
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")

    for usuario in usuarios:
        if usuario['nome'] == nome:
            print("Usuário já existe.")
            return

    novo_usuario = {'nome': nome, 'senha': senha}
    usuarios.append(novo_usuario)
    salvar_usuarios()

    permissoes[nome] = ["ler"]  # Permissões básicas
    salvar_permissoes()

    print(f"Usuário {nome} cadastrado com sucesso.\n")

def login():
    tentativa = 0
    tentativas = 5

    while tentativa < tentativas:
        print("\n--- Login ---")
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")

        for usuario in usuarios:
            if usuario['nome'] == nome and usuario['senha'] == senha:
                print(f"Seja bem-vindo, {nome}")
                return nome

        tentativa += 1
        print("Login ou senha incorretos.")

    print("Login bloqueado.")
    return None

def menu_autenticado(nome_usuario):
    global arquivo_simulado

    while True:
        print(f"\n--- Menu do Usuário ({nome_usuario}) ---")
        print("1 - Ler arquivo (simulado)")
        print("2 - Escrever no arquivo (simulado)")
        print("3 - Apagar arquivo (simulado)")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        acoes = {
            "1": "ler",
            "2": "escrever",
            "3": "apagar"
        }

        if opcao in acoes:
            acao = acoes[opcao]
            if acao in permissoes.get(nome_usuario, []):
                if acao == "ler":
                    print("\n--- Conteúdo do arquivo ---")
                    if arquivo_simulado:
                        print(arquivo_simulado)
                    else:
                        print("[Arquivo vazio]")
                elif acao == "escrever":
                    texto = input("Digite o texto a ser adicionado: ")
                    arquivo_simulado += texto + "\n"
                    print("Texto adicionado ao arquivo simulado.")
                elif acao == "apagar":
                    arquivo_simulado = ""
                    print("Arquivo simulado apagado.")
            else:
                print("Você não tem permissão para essa ação.")
        elif opcao == '4':
            print("Saindo do menu do usuário.")
            break
        else:
            print("Opção inválida.")

# Menu principal
while True:
    print("\n1 - Login")
    print("2 - Cadastro")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        usuario_logado = login()
        if usuario_logado:
            menu_autenticado(usuario_logado)
    elif opcao == '2':
        cadastrar()
    elif opcao == '3':
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")