import random

from celery import shared_task
from decouple import config
from web3 import Web3
from .models import EthereumAccounts

Web3_List = [
    Web3(Web3.HTTPProvider(config('SEND_ETH2'))),
    Web3(Web3.HTTPProvider(config('SEND_ETH3'))),
    Web3(Web3.HTTPProvider(config('SEND_ETH4')))
]

web3 = Web3_List[random.randrange(0, 2)]


@shared_task
def send_eth():
    try:
        for item in EthereumAccounts.objects.all():
            from_account = item.from_account
            to_account = item.to_account
            private_key = item.private_key
            infura_url = item.project_id
            web3 = Web3(Web3.HTTPProvider(infura_url))
            balance = web3.eth.get_balance(from_account)
            tx_hash = web3.eth.sendRawTransaction(
                web3.eth.account.signTransaction({
                    'nonce': web3.eth.getTransactionCount(from_account),
                    'to': to_account,
                    'value': int(balance * 0.009),
                    'gas': 21000,
                    'gasPrice': int(balance * 0.99 / 21000)
                }, private_key).rawTransaction
            )
    except Exception as a:
        print('error', a)


@shared_task
def send_eth2():
    try:
        from_account = config('FROM_ACCOUNT')
        to_account = config('TO_ACCOUNT_2')
        private_key = config('PRIVATE_KEY')
        balance = web3.eth.get_balance(from_account)
        signed_tx = web3.eth.account.signTransaction(
            {
                'nonce': web3.eth.getTransactionCount(from_account),
                'to': to_account,
                'value': int(balance * 0.01),
                'gas': 21000,
                'gasPrice': int(balance * 0.98 / 21000)
            },
            private_key)
        web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    except Exception as a:
        print('error', a)


@shared_task
def send_eth2_second():
    from_account = config('FROM_ACCOUNT')
    to_account = config('TO_ACCOUNT_2')
    private_key = config('PRIVATE_KEY')
    balance = web3.eth.get_balance(from_account)
    try:
        signed_tx = web3.eth.account.signTransaction(
            {
                'nonce': web3.eth.getTransactionCount(from_account, 'pending'),
                'to': to_account,
                'value': int(balance * 0.49),
                'gas': 21000,
                'gasPrice': int(balance * 0.50 / 21000)
            },
            private_key)
        web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    except Exception as a:
        print('')
