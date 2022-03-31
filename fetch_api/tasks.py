from celery import shared_task
from decouple import config
from web3 import Web3
import datetime

x = datetime.datetime.now()
Web3Provider = Web3(Web3.HTTPProvider(config(F'ALCHEMY_DAY_{x.day}')))


@shared_task
def send_eth():
    try:
        from_account = config('FROM_ACCOUNT')
        to_account = config('TO_ACCOUNT_2')
        private_key = config('PRIVATE_KEY')
        web3 = Web3Provider
        balance = web3.eth.get_balance(from_account)
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
    except Exception as a:
        print('error', a)


@shared_task
def send_eth2():
    try:
        from_account = config('FROM_ACCOUNT')
        to_account = config('TO_ACCOUNT_2')
        private_key = config('PRIVATE_KEY')
        web3 = Web3Provider
        balance = web3.eth.get_balance(from_account)
        signed_tx = web3.eth.account.signTransaction(
            {
                'nonce': web3.eth.getTransactionCount(from_account, 'pending'),
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
    web3 = Web3Provider
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
