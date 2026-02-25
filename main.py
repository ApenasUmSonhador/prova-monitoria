# Função auxiliar
def gera_id_sequencial(matriz):
    """Retorna ID sequencial de acordo com o último id_leitor registrado."""
    # Assim, apenas nos casos de exclusão de leitores, pode haver "buracos" na sequência de IDs,
    # mas isso não é um problema para o sistema, pois o ID é apenas um identificador único e não precisa ser contínuo.
    return matriz[0][-1] + 1 if matriz[0] else 1


# Funções obrigatórias
def cadastrar_leitor(leitor, matriz):
    """Registra um novo leitor na matriz, atribuindo um ID sequencial e uma lista vazia de livros lidos."""
    matriz[0].append(
        gera_id_sequencial(matriz)
    )  # Gera e adiciona o ID sequencial à matriz
    matriz[1].append(leitor)  # Adiciona o nome do leitor à matriz
    matriz[2].append([])  # Adiciona lista vazia de livros lidos à matriz
    print(f"Leitor '{leitor}' cadastrado com ID {matriz[0][-1]}.")


def registrar_livro(id_leitor, id_livro, matriz):
    """Registra um livro lido para um leitor específico, identificando o leitor pelo id_leitor."""
    try:
        id_leitor = int(id_leitor)
    except ValueError:
        print("ID do leitor inválido. Deve ser número inteiro.")
        # return matriz
        # Interrompe a função e retorna a matriz sem alterações, mas como não usamos o retorno, farei apenas um return vazio para encerrar a função.
        return

    if id_leitor not in matriz[0]:
        print("Leitor não encontrado.")
        # return matriz
        # Interrompe a função e retorna a matriz sem alterações, mas como não usamos o retorno, farei apenas um return vazio para encerrar a função.
        return

    index_leitor = matriz[0].index(id_leitor)
    try:
        id_livro = int(id_livro)
        if id_livro in matriz[2][index_leitor]:
            print(f"Livro {id_livro} já foi registrado para este leitor.")
        else:
            matriz[2][index_leitor].append(id_livro)
            print(f"Livro {id_livro} registrado para o leitor {id_leitor}.")

    except ValueError:
        print("ID do livro inválido. Deve ser número inteiro.")

    except IndexError:
        print("Leitor não encontrado.")

    # return matriz
    # A função pode retornar a matriz atualizada ou sem alterações dependendo se Ids estão corretos,
    # mas para este sistema, apenas a impressão é necessária.


def mostrar_livros_lidos(id_leitor, matriz):
    """Mostra os livros lidos por um leitor específico, identificando o leitor pelo id_leitor."""
    try:
        index_leitor = matriz[0].index(int(id_leitor))
        livros_lidos = matriz[2][index_leitor]
        print(f"Livros lidos pelo leitor {id_leitor}: ", end="")
        for livro in livros_lidos:
            print(livro, end="; ")
        print()  # Nova linha após a lista de livros
    # return livros_lidos
    # A função pode retornar a lista de livros lidos, mas para este sistema, apenas a impressão é necessária.

    except ValueError:
        print("Leitor não encontrado.")

    # return []
    # Retorna uma lista vazia se o leitor não for encontrado, mas para este sistema, apenas a impressão é necessária.


def mostrar_leitores_por_livro(id_livro, matriz):
    """Mostra os leitores que leram um livro específico, identificando o livro pelo id_livro."""
    try:
        id_livro = int(id_livro)

    except ValueError:
        print("ID do livro inválido. Deve ser número inteiro.")
        # return matriz
        # Interrompe a função e retorna a matriz sem alterações, mas como não usamos o retorno, farei apenas um return vazio para encerrar a função.
        return

    leitores = []
    for i in range(len(matriz[0])):
        if id_livro in matriz[2][i]:
            leitores.append(matriz[1][i])
    if not leitores:
        print(f"Nenhum leitor leu o livro {id_livro}.")
    else:
        print(f"Leitores que leram o livro {id_livro}: {leitores}")

    # return leitores
    # A função pode retornar a lista de leitores, mas para este sistema, apenas a impressão é necessária.


# Funções extras
def arte_em_ascii():
    """
    Exibe arte em ASCII de um livro, para dar um charme ao sistema.
    Créditos para https://ascii-art.botecodigital.dev.br/categorias/objetos/ascii/livro
    """
    print(
        """
         ,..........   ..........,         
     ,..,'          '.'          ',..,     
    ,' ,'            :            ', ',    
   ,' ,'             :             ', ',   
  ,' ,'              :              ', ',  
 ,' ,'............., : ,.............', ', 
,'  '............   '.'   ............'  ',
 '''''''''''''''''';''';'''''''''''''''''' 
                    '''                     
"""
    )


def show_menu():
    """Exibe o menu principal do sistema, com opções para as funcionalidades obrigatórias e extras que foram implementadas."""
    print("Sistema de Gestão de Livros".center(60))
    print("=" * 60)
    arte_em_ascii()
    print("\nPrincipal")
    print("1. Cadastrar novo leitor")
    print("2. Registrar livro lido")
    print("3. Mostrar livros lidos por leitor")
    print("4. Mostrar leitores por livro")
    print("5. Sair")
    print("\nExtra")
    print("6. Apagar livro lido")
    print("7. Apagar todos os livros lidos de um leitor")
    print("8. Apagar leitor")
    print("9. Mostrar matriz atual")
    print("\n" + "=" * 60)


def apagar_livro(id_leitor, id_livro, matriz):
    """Função extra para retirar um livro lido de um leitor específico, identificando o leitor pelo id_leitor e o livro pelo id_livro."""
    try:
        id_leitor = int(id_leitor)
    except ValueError:
        print("ID do leitor inválido. Deve ser número inteiro.")
        return

    try:
        id_livro = int(id_livro)
    except ValueError:
        print("ID do livro inválido. Deve ser número inteiro.")
        return

    try:
        index_leitor = matriz[0].index(id_leitor)
        if id_livro in matriz[2][index_leitor]:
            matriz[2][index_leitor].remove(id_livro)
            print(f"Livro {id_livro} apagado do leitor {id_leitor}.")
        else:
            print("Livro não encontrado na lista de livros lidos do leitor.")

    except ValueError:
        print("Leitor não encontrado.")


def apagar_livros_leitor(id_leitor, matriz):
    """Função extra para apagar todos os livros lidos de um leitor específico, identificando o leitor pelo id_leitor."""
    try:
        index_leitor = matriz[0].index(int(id_leitor))
        matriz[2][index_leitor] = []
        print(f"Todos os livros lidos do leitor {id_leitor} foram apagados.")
    except ValueError:
        print("Leitor não encontrado.")


def apagar_leitor(id_leitor, matriz):
    """Função extra para apagar um leitor específico, identificando o leitor pelo id_leitor. Isso também apaga os livros lidos associados a esse leitor."""
    try:
        index_leitor = matriz[0].index(int(id_leitor))
        matriz[0].pop(index_leitor)
        matriz[1].pop(index_leitor)
        matriz[2].pop(index_leitor)
        print(f"Leitor {id_leitor} apagado com sucesso.")
    except ValueError:
        print("Leitor não encontrado.")


def mostrar_matriz(matriz):
    """Função extra para mostrar a matriz atual de leitores e livros lidos, formatada de maneira legível."""
    print("\n" + "=" * 60)
    print(f"{'ID':<5} | {'Nome Leitor':<20} | {'Livros Lidos':<30}")
    print("=" * 60)
    if not matriz[0]:
        print("Nenhum leitor cadastrado.")
    else:
        for i in range(len(matriz[0])):
            livros = ", ".join(map(str, matriz[2][i])) if matriz[2][i] else "Nenhum"
            print(f"{matriz[0][i]:<5} | {matriz[1][i]:<20} | {livros:<30}")
    print("=" * 60 + "\n")


def main():
    """Função principal que executa o loop do sistema, exibindo o menu e processando as opções escolhidas pelo usuário."""
    # [id_leitor, leitor, livros_lidos]
    matriz = [[], [], []]

    while True:
        show_menu()
        opcao = input("Escolha uma opção: ").strip()

        # Cadastrar de leitor
        if opcao == "1":
            nome_leitor = input("Nome do leitor: ")
            cadastrar_leitor(nome_leitor, matriz)

        # Registrar de livro lido
        elif opcao == "2":
            id_leitor = input("ID do leitor: ")
            id_livro = input("ID do livro: ")
            registrar_livro(id_leitor, id_livro, matriz)

        # Mostrar livros lidos por leitor
        elif opcao == "3":
            id_leitor = input("ID do leitor: ")
            mostrar_livros_lidos(id_leitor, matriz)

        # Mostrar leitores por livro
        elif opcao == "4":
            id_livro = input("ID do livro: ")
            mostrar_leitores_por_livro(id_livro, matriz)

        # Sair
        elif opcao == "5":
            print("Encerrando o sistema...")
            break

        # Apagar livro lido
        elif opcao == "6":
            id_leitor = input("ID do leitor: ")
            id_livro = input("ID do livro a ser apagado: ")
            apagar_livro(id_leitor, id_livro, matriz)

        # Apagar todos os livros lidos de um leitor
        elif opcao == "7":
            id_leitor = input("ID do leitor: ")
            apagar_livros_leitor(id_leitor, matriz)

        # Apagar leitor
        elif opcao == "8":
            id_leitor = input("ID do leitor a ser apagado: ")
            apagar_leitor(id_leitor, matriz)

        # Mostrar matriz atual
        elif opcao == "9":
            mostrar_matriz(matriz)

        # Opção inválida
        else:
            print("Opção inválida.")


# Executa o sistema apenas se este arquivo for executado diretamente, e não importado como módulo em outro arquivo.
# Pois utilizamos as funções em test_main.py, e não queremos que o sistema seja executado durante os testes.
if __name__ == "__main__":
    main()
