# Exercício 11 — Parte 2 — Implementação dos Testes de Aceitação (Glue Code + Smart Contract)

Estudo dirigido **INE5455-Testes-32**, **Parte 2**: implementação do **código de cola
(glue code)** com [Behave](https://behave.readthedocs.io/) (Python + Gherkin) e conclusão
do **smart contract** em Solidity (`ClientContractorContract`), de forma que os testes de
aceitação especificados na Parte 1 sejam executados **com sucesso**.

O contrato é compilado com [py-solc-x](https://pypi.org/project/py-solc-x/) e implantado
numa blockchain Ethereum local via [web3.py](https://web3py.readthedocs.io/).

O contrato modela a relação entre **contratante** (client) e **contratada** (contractor):
data de assinatura e o ciclo de vida do contrato
(`Created` → `InEffect` → `SuccessfulTermination` / `UnsuccessfulTermination`).
Por ora, o glue cobre a parte de **criação/ativação** (`Created` → `InEffect`).

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
padrão. Além disso, o glue **assina as transações com uma conta fixa** (`address` /
`private_key` no topo de `create-AAA-BBB-contract.py`). Por padrão o Ganache cria contas
aleatórias, então essa conta não existiria — e o deploy falharia. É preciso **semear a
conta** com a chave privada do glue e saldo via `--wallet.accounts <chave>,<saldo_wei>`.

Suba na porta `7545`, com `Gas Limit = 9000000`, `Gas Price = 4100000000`, `chainId = 1337`
(igual ao `chain_id` do glue) e a conta do glue semeada com 1000 ETH:

```bash
npx ganache \
  -p 7545 \
  --chain.chainId 1337 \
  --miner.blockGasLimit 9000000 \
  --miner.defaultGasPrice 4100000000 \
  --wallet.accounts 0x65003de1163f6c193dd214b5d3fdfa7a7d79afacc0114d81d565ae1e7a04f562,1000000000000000000000
```

> O endereço `0xDfDb2B6FdF25F7A0850AfBd369A69f5d6819587E` é **derivado** dessa chave
> privada — por isso basta passar a chave; o Ganache calcula o endereço. `1000000000000000000000`
> = 1000 ETH em wei (10²¹), só para cobrir o gás.

Deixe esse processo rodando num terminal e rode os testes noutro.

## Configuração obrigatória

O glue code (`tests/features/steps/create-AAA-BBB-contract.py`) usa:

- **Conta e chave** (`address`, `private_key`): a conta semeada no comando do Ganache
  acima. Se trocar a chave no glue, troque também no `--wallet.accounts`. `chain_id = 1337`
  precisa bater com o `--chain.chainId` do Ganache.
- **Caminho do `.sol`**: relativo (`src/resources/ClientContractorContract.sol`) — rode o
  `behave` a partir da raiz do projeto (`exercicio_11_parte_2/`).

> Sem o Ganache rodando — ou com a conta do glue **sem saldo** — os cenários dão **erro**
> na etapa de deploy (`When o contrato passa a existir` / `Given o contrato existe`).

## Execução

Com o Ganache rodando, a partir da raiz do projeto.

A feature de criação (glue implementado, **passa**):

```bash
uv run behave tests/features/CreateAAABBBContract.feature
```

Filtros úteis:

```bash
# Por tag
uv run behave --tags=@CreateContract
uv run behave --tags=@ActivateContract

# Por nome de cenário (regex)
uv run behave -n "O contrato é registrado"

# Parar no primeiro erro
uv run behave --stop
```

> A feature `TerminateAAABBBContract.feature` **ainda não tem glue** (os passos de
> terminação dependem de funções de encerramento no `.sol`). Rodar `uv run behave` sem
> filtro reporta esses passos como *undefined*.

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
| `ClientContractorContract.sol`      | Construtor (client/contractor/data), `activate` e getters `view` (`getStatus`, `isActivated`). |
| `CreateAAABBBContract.feature`      | `Background` (partes + data) + cenários **criar** (`@CreateContract`) e **ativar** (`@ActivateContract`). |
| `TerminateAAABBBContract.feature`   | Terminação com **sucesso** e `Scenario Outline` de **insucesso** (glue pendente).             |
| `create-AAA-BBB-contract.py`        | Glue: compila o `.sol` (`solcx`), deploya via `web3.py` e dirige/consulta o contrato.        |

## Fluxo do teste (criação)

1. `Background` define contratante, contratada e a data de assinatura no `context`.
2. `When o contrato passa a existir` (e `Given o contrato existe`) → compila o `.sol`
   (`solcx`), monta e assina a transação de deploy, e envia para o Ganache (`web3.py`).
3. `When o contrato é ativado` → envia a transação `activate()` (modifica estado → `InEffect`).
4. Passos `Then` chamam getters `view` via `.call()` (`isActivated`, `getStatus`) e comparam
   com os valores esperados (`STATUS` mapeia o nome do estado para o índice do `enum`).
