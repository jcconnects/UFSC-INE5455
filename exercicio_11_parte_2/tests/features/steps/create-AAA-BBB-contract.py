from behave import *
from unittest import TestCase

from solcx import compile_standard, install_solc
import json
from web3 import Web3

address = "0xDfDb2B6FdF25F7A0850AfBd369A69f5d6819587E"
private_key = "0x65003de1163f6c193dd214b5d3fdfa7a7d79afacc0114d81d565ae1e7a04f562"

smart_contract = None
w3 = None
chain_id = 1337

# Status do contrato (enum no smart contract)
STATUS = {
    "Created": 0,
    "InEffect": 1,
    "SuccessfulTermination": 2,
    "UnsuccessfulTermination": 3,
}


def __deploy_contract(client, contractor, creation_date):
    global smart_contract
    global w3

    with open("src/resources/ClientContractorContract.sol", "r") as file:
        smart_contract_file = file.read()
    _solc_version = "0.8.0"
    install_solc(_solc_version)
    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {
                "ClientContractorContract.sol": {"content": smart_contract_file}
            },
            "settings": {
                "outputSelection": {
                    "*": {
                        "*": [
                            "abi",
                            "metadata",
                            "evm.bytecode",
                            "evm.bytecode.sourceMap",
                        ]
                    }
                }
            },
        },
        solc_version=_solc_version,
    )
    with open("compiled_code.json", "w") as file:
        json.dump(compiled_sol, file)
    bytecode = compiled_sol["contracts"]["ClientContractorContract.sol"][
        "ClientContractorContract"
    ]["evm"]["bytecode"]["object"]
    abi = json.loads(
        compiled_sol["contracts"]["ClientContractorContract.sol"][
            "ClientContractorContract"
        ]["metadata"]
    )["output"]["abi"]
    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    transaction = contract.constructor(
        client, contractor, creation_date
    ).build_transaction(
        {
            "chainId": chain_id,
            "gasPrice": w3.eth.gas_price,
            "from": address,
            "nonce": w3.eth.get_transaction_count(address),
        }
    )
    signed = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    smart_contract = w3.eth.contract(address=receipt.contractAddress, abi=abi)


# Envia uma transação que modifica o estado do contrato (não é view)
def __send_tx(contract_function):
    transaction = contract_function.build_transaction(
        {
            "chainId": chain_id,
            "gasPrice": w3.eth.gas_price,
            "from": address,
            "nonce": w3.eth.get_transaction_count(address),
        }
    )
    signed = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
    w3.eth.wait_for_transaction_receipt(tx_hash)


# GIVEN (Background)


@given("a AAA Consultoria Empresarial é a contratante")
def step_impl(context):
    context.client = "AAA Consultoria Empresarial"


@given("a BBB Tecnologia é a contratada")
def step_impl(context):
    context.contractor = "BBB Tecnologia"


@given("o contrato é assinado no dia {dia}")
def step_impl(context, dia):
    context.creation_date = int(dia)


# GIVEN (pré-condições: contrato já existe / já está ativo)


@given("o contrato existe")
def step_impl(context):
    __deploy_contract(context.client, context.contractor, context.creation_date)


@given("o contrato está ativo")
def step_impl(context):
    __send_tx(smart_contract.functions.activate())


# WHEN


@when("o contrato passa a existir")
def step_impl(context):
    __deploy_contract(context.client, context.contractor, context.creation_date)


@when("o contrato é ativado")
def step_impl(context):
    __send_tx(smart_contract.functions.activate())


# WHEN (encerramento — obrigações sendo cumpridas ou descumpridas)


@when("a contratada presta os serviços contratados")
def step_impl(context):
    __send_tx(smart_contract.functions.provideServices())


@when("a contratante paga metade do serviço na assinatura do contrato")
def step_impl(context):
    __send_tx(smart_contract.functions.payFirstHalf())


@when("a contratante paga a outra metade trinta dias após o início dos trabalhos")
def step_impl(context):
    __send_tx(smart_contract.functions.paySecondHalf())


@when("a parte responsável não cumpre sua obrigação")
def step_impl(context):
    __send_tx(smart_contract.functions.breach())


# THEN


@then("o contrato não está ativo")
def step_impl(context):
    TestCase().assertFalse(smart_contract.functions.isActivated().call())


@then("o contrato está ativo")
def step_impl(context):
    TestCase().assertTrue(smart_contract.functions.isActivated().call())


@then('o estado do contrato é "{estado}"')
def step_impl(context, estado):
    TestCase().assertEqual(STATUS[estado], smart_contract.functions.getStatus().call())
