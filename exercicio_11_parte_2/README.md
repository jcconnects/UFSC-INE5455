# Exercício 11 — Parte 2 — Implementação dos Testes de Aceitação (Glue Code + Smart Contract)

Estudo dirigido **INE5455-Testes-32**, **Parte 2**: implementação do **código de cola
(glue code)** com [Behave](https://behave.readthedocs.io/) (Python + Gherkin) e conclusão
do **smart contract** em Solidity (`ClientContractorContract`), de forma que os testes de
aceitação especificados na Parte 1 sejam executados **com sucesso**.

O contrato é compilado com [py-solc-x](https://pypi.org/project/py-solc-x/) e implantado
numa blockchain Ethereum local via [web3.py](https://web3py.readthedocs.io/).

O contrato modela a relação entre **contratante** (client) e **contratada** (contractor):
datas (criação, início, término), lista de **obrigações** de cada parte, e o ciclo de vida
do contrato (`Created` → `InEffect` → `SuccessfulTermination` / `UnsuccessfulTermination`).

## Parte 1 vs. Parte 2

- **Parte 1**: especificação dos testes de aceitação em arquivos `.feature` (Gherkin).
- **Parte 2** (este projeto): implementar o **glue code** (`steps/`) e **completar o smart
  contract** (`.sol`) para que os cenários da Parte 1 passem.

## Pré-requisitos

1. [uv](https://docs.astral.sh/uv/) para dependências Python (`>=3.13`).
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

Antes de rodar, ajuste o glue code em `tests/features/steps/create-AAA-BBB-contract.py`:

- **Conta e chave** (`address`, `private_key`): devem corresponder a uma conta com saldo
  na sua instância do Ganache. `chain_id = 1337` é o padrão do Ganache.
- **Caminho do `.sol`**: o glue abre o `ClientContractorContract.sol` por caminho. Use um
  caminho relativo (`src/resources/ClientContractorContract.sol`) ou ajuste o absoluto
  para a sua máquina.

> Sem o Ganache rodando, os cenários falham na etapa `When o contrato é criado` (deploy).

## Execução

Todos os testes:

```bash
uv run behave
```

Uma feature específica:

```bash
uv run behave tests/features/CreateAAABBBContract.feature
uv run behave tests/features/TerminateAAABBBContract.feature
```

Filtros úteis:

```bash
# Por tag
uv run behave --tags=@CreateContract
uv run behave --tags=@ActivateContract
uv run behave --tags=@SuccessfullyTerminateContract
uv run behave --tags=@UnsuccessfullyTerminateContract

# Por nome de cenário (regex)
uv run behave -n "Create the SC_AAA_BBB contract"

# Parar no primeiro erro
uv run behave --stop
```

## Implementação da Parte 2

### Glue code (`steps/`)

Regras (do enunciado da Parte 2):

- **Uma função por notação.** Mesmo que o texto do passo seja igual entre `Given`, `When`
  e `Then`, cada notação precisa da sua própria função decorada (`@given` / `@when` /
  `@then`).
- **`call()` vs. `build_transaction()`.** Função que **não modifica** o contrato (getter
  `view`) é chamada via `.call()`. Função que **modifica** o estado (deploy, `activate`,
  satisfazer obrigação) é enviada via `.build_transaction()` → `sign_transaction` →
  `send_raw_transaction` → `wait_for_transaction_receipt`.
- O `context` do Behave carrega os dados entre passos (contratante, contratada, datas,
  obrigações).

### Smart contract (`.sol`)

A superfície do contrato deriva diretamente dos passos das features:

- **Estado**: `enum Status { Created, InEffect, SuccessfulTermination, UnsuccessfulTermination }`,
  exposto por `getStatus()`.
- **Datas**: criação, início e término (getters `view`).
- **Obrigações**: adicionar obrigação da **contratada** / **contratante**; consultar se
  uma obrigação **existe** e se **está ativada**; **satisfazer** uma obrigação.
- **`activate()`**: ativa o contrato (`InEffect`) e suas obrigações. A `oblig7` (pacote de
  20 h após o período de garantia) **só ativa** quando sua condição temporal é atingida —
  permanece desativada na ativação inicial.
- **Terminação**:
  - **Sucesso** quando as obrigações de pagamento/serviço são satisfeitas
    (`oblig1`, `oblig4`, `oblig5`) → `SuccessfulTermination`.
  - **Insucesso** quando qualquer obrigação exigida (`oblig1`, `oblig2`, `oblig4`,
    `oblig5`) **não** é satisfeita → `UnsuccessfulTermination`.

Dicas do enunciado:

- Operador booleano **AND** em Solidity é `&&` — ex.: `if ((A) && (B)) {...}`.
- Por simplificação, considere **apenas os dias** das datas que aparecem no contrato
  (ex.: dia 10, 30, 50, 80, ...).

## Conteúdo

| Item                                | O que cobre                                                                                  |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| `ClientContractorContract.sol`      | Construtor (client/contractor/datas), obrigações, `activate`, satisfação e ciclo de vida.    |
| `CreateAAABBBContract.feature`      | `Background` (partes + datas + obrigações) + cenários **criar** e **ativar** contrato.       |
| `TerminateAAABBBContract.feature`   | `Background` (cria + ativa) + terminação com **sucesso** e `Scenario Outline` de **insucesso**. |
| `create-AAA-BBB-contract.py`        | Glue: compila o `.sol` (`solcx`), deploya via `web3.py` e dirige/consulta o contrato.        |

## Fluxo do teste

1. `Background` define contratante, contratada, datas e obrigações no `context`.
2. `When o contrato é criado` → compila o contrato (`solcx`), monta e assina a transação
   de deploy, e envia para o Ganache (`web3.py`).
3. `When o contrato é ativado` → envia a transação `activate()` (modifica estado).
4. Passos de obrigação (`"obligN" é satisfeita` / `não é satisfeita`) enviam transações que
   mudam o estado de cada obrigação e, ao final, o `Status` do contrato.
5. Passos `Then` chamam getters `view` via `.call()` (`getStatus`, existência/ativação de
   obrigação, etc.) e comparam com os valores esperados.
