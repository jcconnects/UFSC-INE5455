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


def __deploy_contract(client, contractor, creation_date):
    global smart_contract
    global w3

    # Endereço do diretório onde está o smart contract AAABBBContract
    with open("/Users/vilain/Dropbox/Pos-Sabbatical-Project/Implementation-SmartContract-AAA-BBB-Python/src/resources/ClientContractorContract.sol", "r") as file:
        smart_contract_file = file.read()
    _solc_version = "0.8.0"
    install_solc(_solc_version)
    # Considerando o smart contract ProductSaleContract
    compiled_sol = compile_standard({"language": "Solidity", "sources": {"ClientContractorContract.sol": {"content": smart_contract_file}},
            "settings": {"outputSelection": {"*": {"*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]} } }, }, solc_version=_solc_version,)
    with open("compiled_code.json", "w") as file:
        json.dump(compiled_sol, file)
    bytecode = compiled_sol["contracts"]["ClientContractorContract.sol"]["ClientContractorContract"]["evm"]["bytecode"]["object"]
    abi = json.loads(compiled_sol["contracts"]["ClientContractorContract.sol"]["ClientContractorContract"]["metadata"])["output"]["abi"]
    # Rodando o ganache localmente...
    w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
    smart_contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    nonce = w3.eth.get_transaction_count(address)
    # Parâmetros do construtor do smart contract
    transaction = smart_contract.constructor(client, contractor, creation_date).build_transaction(
        {"chainId": chain_id, "gasPrice": w3.eth.gas_price, "from": address, "nonce": nonce})
    sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.raw_transaction)
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
    # Referência para o smart contract
    smart_contract = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)


@given(u'the client named {client}')
def step_impl(context, client):
    context.client = "AAA"


@given(u'the contractor named {contractor}')
def step_impl(context, contractor):
    context.contractor = contractor


@given(u'the creation date is {date}')
def step_impl(context, date):
    context.creation_date = int(date)


@given(u'I have created and deployed the smart contract')
def step_impl(context):
    __deploy_contract(context.client, context.contractor, context.creation_date)


@when(u'I activate the smart contract')
def step_impl(context):
    transaction = smart_contract.functions.activate().build_transaction({"chainId": chain_id,
                                                                         "gasPrice": w3.eth.gas_price,
                                                                         "from": address,
                                                                         "nonce": w3.eth.get_transaction_count(address)})
    sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.raw_transaction)


@then(u'the smart contract is activated')
def step_impl(context):
    status = smart_contract.functions.getStatus().call()
    TestCase.assertEqual(TestCase(), 1, status)  # Status.InEffect = 1


@then(u'creation date is {date}')
def step_impl(context, date):
    TestCase.assertEqual(TestCase(), int(date), smart_contract.functions.getCreationDate().call())
