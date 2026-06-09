# Exercício 10 — Testes de Aceitação com Behave

Estudo dirigido **INE5455-Testes-32**: testes de aceitação BDD usando o framework
[Behave](https://behave.readthedocs.io/) com Python e linguagem Gherkin, sobre o domínio
**Mercado de Leilão**.

## Estrutura

```
exercicio_10/
├── src/                                    # Código da aplicação (mercado de leilão)
│   ├── mercado_leilao.py
│   ├── usuario.py
│   ├── produto.py
│   ├── produto_leilao.py
│   └── lance.py
├── tests/
│   └── features/                           # Arquivos .feature (Gherkin)
│       ├── CadastrarUsuario_Test.feature
│       ├── CadastrarConjuntoUsuarios_Test.feature
│       ├── CadastrarProduto_Test.feature   # Exercício (Background + 2 cenários)
│       ├── environment.py                  # Bootstrap de sys.path (src/)
│       └── steps/                          # Glue code (.py)
│           ├── cadastrar_usuario_test.py
│           ├── cadastrar_conjunto_de_usuarios_test.py
│           └── cadastrar_produto_test.py
├── behave.ini
├── pyproject.toml
└── README.md
```

## Setup

Requer [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

## Execução

Todos os testes:

```bash
uv run behave
```

Uma feature específica (passe o caminho):

```bash
uv run behave tests/features/CadastrarUsuario_Test.feature
uv run behave tests/features/CadastrarConjuntoUsuarios_Test.feature
uv run behave tests/features/CadastrarProduto_Test.feature
```

Outros filtros úteis:

```bash
# Por nome de cenário (regex)
uv run behave -n "Cadastrar Usuario com Sucesso"

# Por tag (adicione @tag acima do Scenario/Feature primeiro)
uv run behave --tags=@smoke

# Parar no primeiro erro
uv run behave --stop
```

## Conteúdo

| Feature                                 | O que cobre                                                                 |
|-----------------------------------------|-----------------------------------------------------------------------------|
| `CadastrarUsuario_Test.feature`         | Cenário simples: cadastro de um usuário.                                    |
| `CadastrarConjuntoUsuarios_Test.feature`| `Scenario Outline` parametrizado (sucesso e CPF inválido).                  |
| `CadastrarProduto_Test.feature`         | Exercício do PDF: `Background` + cadastro normal + cadastro duplicado.      |
