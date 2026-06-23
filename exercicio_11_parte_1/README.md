# Exercício 11 — Testes de Aceitação sobre Smart Contract (Solidity)

Estudo dirigido **INE5455-Testes-32**: testes de aceitação BDD com
[Behave](https://behave.readthedocs.io/) (Python + Gherkin) sobre um **smart contract**
em Solidity (`ProductSaleContract`), compilado com [py-solc-x](https://pypi.org/project/py-solc-x/)
e implantado numa blockchain Ethereum local via [web3.py](https://web3py.readthedocs.io/).

O contrato modela uma venda entre **seller** e **buyer**, com título, moeda
(`USD`/`CAN`/`BRL`) e lista de produtos. Os cenários criam o contrato e verificam
os getters via chamadas `.call()`.

## Pré-requisitos

1. [uv](https://docs.astral.sh/uv/) para dependências Python.
2. [Node.js](https://nodejs.org/) + npm, para instalar o [Ganache](https://github.com/ConsenSys-archive/ganache#readme)
   (blockchain Ethereum local).
3. O `solc` 0.8.0 é baixado automaticamente pelo `py-solc-x` na primeira execução.

```bash
uv sync

# Ganache (npm, instalação local no projeto)
npm init -y          # cria package.json, se ainda não existir
npm install ganache  # instala em node_modules/ (sem --global)
```

### Subir o Ganache (CLI)

As instruções do exercício usam o **Ganache GUI** (opção *Quickstart* + ajuste de
*Gas Limit* / *Gas Price* no menu Settings → aba Chain). Aqui usamos o **Ganache CLI**,
então não há menu: os mesmos valores viram **flags** na linha de comando.

O glue code aponta para `HTTP://127.0.0.1:7545`, mas o Ganache ouve em `8545` por
padrão. Suba na porta `7545` com `Gas Limit = 9000000` e `Gas Price = 4100000000`:

```bash
npx ganache \
  -p 7545 \
  --miner.blockGasLimit 9000000 \
  --miner.defaultGasPrice 4100000000
```

Deixe esse processo rodando num terminal e rode os testes noutro.

## Configuração obrigatória

Antes de rodar, ajuste o glue code em `tests/features/steps/create-product-sale-contract.py`:

- **Conta e chave** (`address`, `private_key`): devem corresponder a uma conta
  com saldo na sua instância do Ganache. `chain_id = 1337` é o padrão do Ganache.

> Sem o Ganache rodando, os cenários falham na etapa
> `When the contract is created` (deploy).

## Execução

Todos os testes:

```bash
uv run behave
```

A feature específica:

```bash
uv run behave tests/features/CreateProductSaleContract.feature
```

Filtros úteis:

```bash
# Por tag
uv run behave --tags=@CreateProductSaleContract
uv run behave --tags=@CreateSeveralProductSaleContracts

# Por nome de cenário (regex)
uv run behave -n "Create a product sale contract succeeding"

# Parar no primeiro erro
uv run behave --stop
```

## Conteúdo

| Item                                       | O que cobre                                                                      |
|--------------------------------------------|----------------------------------------------------------------------------------|
| `ProductSaleContract.sol`                  | Contrato com construtor (seller/buyer/title/currency) e getters `view`.          |
| `CreateProductSaleContract.feature`        | `Background` (seller/buyer/data) + cenário de sucesso + `Scenario Outline` (USD/CAN/BRL). |
| `create-product-sale-contract.py`          | Compila o `.sol`, deploya via web3 e valida seller, buyer, title, currency e preço total. |

## Fluxo do teste

1. `Background` define seller, buyer e data efetiva no `context`.
2. `When the contract is created` → compila o contrato (`solcx`), monta e assina a
   transação de deploy, e envia para o Ganache (`web3.py`).
3. Os passos `Then` chamam os getters (`getSeller`, `getBuyer`, `getTitle`,
   `getCurrency`, `getContractTotalPrice`) e comparam com os valores esperados.
   A moeda é mapeada para o `enum` (`USD=0`, `CAN=1`, `BRL=2`).
</content>
</invoke>
