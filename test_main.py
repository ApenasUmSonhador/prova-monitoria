import pytest
from main import (
    gera_id_sequencial,
    cadastrar_leitor,
    registrar_livro,
    mostrar_livros_lidos,
    mostrar_leitores_por_livro,
    retirar_livro as apagar_livro,
    apagar_livros_leitor,
    apagar_leitor,
)

# =====================================================
# FIXTURES
# =====================================================


@pytest.fixture
def matriz_vazia():
    return [[], [], []]


@pytest.fixture
def matriz_com_leitores():
    matriz = [[], [], []]
    cadastrar_leitor("Ana", matriz)
    cadastrar_leitor("João", matriz)
    cadastrar_leitor("Carlos", matriz)
    return matriz


# =====================================================
# TESTES GERAÇÃO ID
# =====================================================


@pytest.mark.parametrize(
    "matriz, esperado",
    [
        ([[], [], []], 1),
        ([[1], ["Ana"], [[]]], 2),
        ([[1, 2, 3], ["A", "B", "C"], [[], [], []]], 4),
    ],
)
def test_gera_id_sequencial_varios(matriz, esperado):
    assert gera_id_sequencial(matriz) == esperado


# =====================================================
# TESTES CADASTRO
# =====================================================


def test_cadastrar_leitor_basico(matriz_vazia):
    cadastrar_leitor("Ana", matriz_vazia)
    assert matriz_vazia[0] == [1]
    assert matriz_vazia[1] == ["Ana"]
    assert matriz_vazia[2] == [[]]


def test_cadastrar_varios_leitores(matriz_vazia):
    nomes = ["Ana", "João", "Carlos", "Maria"]
    for nome in nomes:
        cadastrar_leitor(nome, matriz_vazia)

    assert matriz_vazia[0] == [1, 2, 3, 4]
    assert matriz_vazia[1] == nomes
    assert len(matriz_vazia[2]) == 4


# =====================================================
# TESTES REGISTRAR LIVRO
# =====================================================


@pytest.mark.parametrize("livro", [10, 20, 30])
def test_registrar_livro_valores_diferentes(matriz_com_leitores, livro):
    registrar_livro(1, livro, matriz_com_leitores)
    assert livro in matriz_com_leitores[2][0]


def test_registrar_livro_multiplos(matriz_com_leitores):
    livros = [1, 2, 3, 4]
    for livro in livros:
        registrar_livro(1, livro, matriz_com_leitores)

    assert matriz_com_leitores[2][0] == livros


def test_registrar_livro_duplicado(matriz_com_leitores, capsys):
    registrar_livro(1, 99, matriz_com_leitores)
    registrar_livro(1, 99, matriz_com_leitores)
    captured = capsys.readouterr()
    assert "já foi registrado" in captured.out


@pytest.mark.parametrize("id_invalido", ["abc", "", None])
def test_registrar_livro_id_invalido(matriz_com_leitores, capsys, id_invalido):
    registrar_livro(id_invalido, 10, matriz_com_leitores)
    captured = capsys.readouterr()
    assert "ID do leitor inválido" in captured.out


# =====================================================
# TESTES MOSTRAR LIVROS
# =====================================================


def test_mostrar_livros_varios(matriz_com_leitores, capsys):
    registrar_livro(1, 10, matriz_com_leitores)
    registrar_livro(1, 20, matriz_com_leitores)

    mostrar_livros_lidos(1, matriz_com_leitores)
    captured = capsys.readouterr()

    assert "10" in captured.out
    assert "20" in captured.out


@pytest.mark.parametrize("leitor_inexistente", [999, -1, 0])
def test_mostrar_livros_leitor_inexistente(
    matriz_com_leitores, capsys, leitor_inexistente
):
    mostrar_livros_lidos(leitor_inexistente, matriz_com_leitores)
    captured = capsys.readouterr()
    assert "Leitor não encontrado" in captured.out


# =====================================================
# TESTES MOSTRAR LEITORES POR LIVRO
# =====================================================


def test_multiplos_leitores_mesmo_livro(matriz_com_leitores, capsys):
    registrar_livro(1, 500, matriz_com_leitores)
    registrar_livro(2, 500, matriz_com_leitores)

    mostrar_leitores_por_livro(500, matriz_com_leitores)
    captured = capsys.readouterr()

    assert "Ana" in captured.out
    assert "João" in captured.out


@pytest.mark.parametrize("livro_inexistente", [888, 777])
def test_mostrar_leitores_livro_inexistente(
    matriz_com_leitores, capsys, livro_inexistente
):
    mostrar_leitores_por_livro(livro_inexistente, matriz_com_leitores)
    captured = capsys.readouterr()
    assert "Nenhum leitor leu o livro" in captured.out


# =====================================================
# TESTES APAGAR LIVRO
# =====================================================


@pytest.mark.parametrize("livro", [10, 20, 30])
def test_apagar_livros_diferentes(matriz_com_leitores, livro):
    registrar_livro(1, livro, matriz_com_leitores)
    apagar_livro(1, livro, matriz_com_leitores)
    assert livro not in matriz_com_leitores[2][0]


def test_apagar_livro_nao_existente(matriz_com_leitores, capsys):
    apagar_livro(1, 999, matriz_com_leitores)
    captured = capsys.readouterr()
    assert "Livro não encontrado" in captured.out


# =====================================================
# TESTES APAGAR TODOS LIVROS
# =====================================================


def test_apagar_livros_varios(matriz_com_leitores):
    registrar_livro(1, 1, matriz_com_leitores)
    registrar_livro(1, 2, matriz_com_leitores)

    apagar_livros_leitor(1, matriz_com_leitores)
    assert matriz_com_leitores[2][0] == []


# =====================================================
# TESTES APAGAR LEITOR
# =====================================================


def test_apagar_leitor_meio_lista(matriz_com_leitores):
    apagar_leitor(2, matriz_com_leitores)

    assert 2 not in matriz_com_leitores[0]
    assert len(matriz_com_leitores[0]) == 2


@pytest.mark.parametrize("leitor_inexistente", [999, -10])
def test_apagar_leitor_inexistente(matriz_com_leitores, capsys, leitor_inexistente):
    apagar_leitor(leitor_inexistente, matriz_com_leitores)
    captured = capsys.readouterr()
    assert "Leitor não encontrado" in captured.out


# =====================================================
# TESTES INTEGRIDADE
# =====================================================


def test_integridade_matriz(matriz_com_leitores):
    registrar_livro(1, 100, matriz_com_leitores)
    apagar_leitor(2, matriz_com_leitores)

    assert len(matriz_com_leitores[0]) == len(matriz_com_leitores[1])
    assert len(matriz_com_leitores[1]) == len(matriz_com_leitores[2])


def test_id_sequencial_apos_remocao(matriz_com_leitores):
    apagar_leitor(3, matriz_com_leitores)
    cadastrar_leitor("Novo", matriz_com_leitores)

    assert matriz_com_leitores[0][-1] == 4


# =====================================================
# TESTE DE VOLUME
# =====================================================


def test_cadastro_em_massa(matriz_vazia):
    for i in range(100):
        cadastrar_leitor(f"Leitor{i}", matriz_vazia)

    assert len(matriz_vazia[0]) == 100
    assert matriz_vazia[0][0] == 1
    assert matriz_vazia[0][-1] == 100
