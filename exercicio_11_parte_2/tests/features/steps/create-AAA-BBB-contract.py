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
STATUS = {"Created": 0, "InEffect": 1, "SuccessfulTermination": 2, "UnsuccessfulTermination": 3}


def __deploy_contract(client, contractor, creation_date):
    global smart_contract
    global w3

    with open("src/resources/ClientContractorContract.sol", "r") as file:
        smart_contract_file = file.read()
    _solc_version = "0.8.0"
    install_solc(_solc_version)
    compiled_sol = compile_standard({"language": "Solidity", "sources": {"ClientContractorContract.sol": {"content": smart_contract_file}},
            "settings": {"outputSelection": {"*": {"*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]} } }, }, solc_version=_solc_version,)
    with open("compiled_code.json", "w") as file:
        json.dump(compiled_sol, file)
    bytecode = compiled_sol["contracts"]["ClientContractorContract.sol"]["ClientContractorContract"]["evm"]["bytecode"]["object"]
    abi = json.loads(compiled_sol["contracts"]["ClientContractorContract.sol"]["ClientContractorContract"]["metadata"])["output"]["abi"]
    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    transaction = contract.constructor(client, contractor, creation_date).build_transaction(
        {"chainId": chain_id, "gasPrice": w3.eth.gas_price, "from": address, "nonce": w3.eth.get_transaction_count(address)})
    signed = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    smart_contract = w3.eth.contract(address=receipt.contractAddress, abi=abi)


def __activate_contract():
    transaction = smart_contract.functions.activate().build_transaction(
        {"chainId": chain_id, "gasPrice": w3.eth.gas_price, "from": address, "nonce": w3.eth.get_transaction_count(address)})
    signed = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
    w3.eth.wait_for_transaction_receipt(tx_hash)


# GIVEN (Background)

@given(u'a AAA Consultoria Empresarial é a contratante')
def step_impl(context):
    context.client = "AAA Consultoria Empresarial"


@given(u'a BBB Tecnologia é a contratada')
def step_impl(context):
    context.contractor = "BBB Tecnologia"


@given(u'o contrato é assinado no dia {dia}')
def step_impl(context, dia):
    context.creation_date = int(dia)


# GIVEN (pré-condição: contrato já existe)

@given(u'o contrato existe')
def step_impl(context):
    __deploy_contract(context.client, context.contractor, context.creation_date)


# WHEN

@when(u'o contrato passa a existir')
def step_impl(context):
    __deploy_contract(context.client, context.contractor, context.creation_date)


@when(u'o contrato é ativado')
def step_impl(context):
    __activate_contract()


# THEN

@then(u'o contrato não está ativo')
def step_impl(context):
    TestCase().assertFalse(smart_contract.functions.isActivated().call())


@then(u'o contrato está ativo')
def step_impl(context):
    TestCase().assertTrue(smart_contract.functions.isActivated().call())


@then(u'o estado do contrato é "{estado}"')
def step_impl(context, estado):
    TestCase().assertEqual(STATUS[estado], smart_contract.functions.getStatus().call())
