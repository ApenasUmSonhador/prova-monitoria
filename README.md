# Sistema de Gestão de Leitores e Livros

Sistema em Python para gerenciamento de leitores e livros lidos, com menu interativo e suíte completa de testes automatizados usando pytest.

## Contexto da Prova de Monitoria

O sistema de gestão de livros é uma plataforma digital onde leitores registram os livros que já leram,
permitindo acompanhar seu histórico de leitura.
Você foi escolhido para desenvolver o módulo de gerenciamento de leitura de livros. Este módulopermite que cada leitor se cadastre e registre os livros que ele já leu.

## Funcionalidades

O sistema permite...

### Funcionalidades principais

- Cadastrar leitor
- Gerar ID sequencial automático
- Registrar livro lido
- Listar livros lidos por leitor
- Listar leitores por livro

### Funcionalidades extras

- Remover livro de um leitor
- Apagar todos os livros de um leitor
- Apagar leitor
- Visualizar matriz interna
- Interface com arte ASCII

## Estrutura de Dados

O sistema utiliza uma matriz 3xN:

```py
[
    [ids],
    [nomes],
    [listas_de_livros]
]
```

**Exemplo:**

```py
[
    [1, 2, 3],
    ["Alice", "Bob", "Charlie"],
    [["292", "43"], ["9289"], []]
]
```

Isso significa:

- Alice (ID 1) leu os livros 292 e 43
- Bob (ID 2) leu o livro 9289
- Charlie (ID 3) não leu nenhum livro

## Estrutura do Projeto

```yml
projeto/
│
├── main.py
├── test_main.py
└── README.md
```

## Instruções para Execução

No terminal:

```bash
python main.py
```

Depois, siga as instruções do menu para interagir com o sistema.

Instale pytest:

```bash
pip install pytest
```

Execute os testes:

```bash
python -m pytest -v
```

**Cobertura:** IDs, cadastro, registros, duplicatas, validações, remoções, integridade estrutural e fluxos completos.

## Tratamento de Erros

- ID inválido (não inteiro)
- Leitor inexistente
- Livro duplicado
- Remoção de item inexistente
- Estrutura sempre consistente

## Considerações Finais

O sistema foi projetado para ser simples, eficiente e fácil de usar, com foco na funcionalidade principal de gerenciamento de leitores e livros lidos, além de uma suíte de testes robusta para garantir a qualidade do código.

Tentei não utilizar recursos avançados de Python nem bibliotecas externas, mantendo o código acessível e fácil de entender, mesmo para quem está começando a programar, que é a ideia de Fundamentos de Programação.
