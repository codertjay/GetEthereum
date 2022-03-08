from celery import shared_task
from decouple import config
from web3 import Web3
from .models import EthereumAccounts


@shared_task
def send_eth():
    try:
        for item in EthereumAccounts.objects.all():
            from_account = Web3.toChecksumAddress(item.from_account)
            to_account = Web3.toChecksumAddress(item.to_account)
            private_key = item.private_key
            infura_url = item.project_id
            web3 = Web3(Web3.HTTPProvider(infura_url))
            balance = web3.eth.get_balance(from_account)
            nonce = web3.eth.getTransactionCount(from_account)
            try:
                gasPrice = int(balance * 0.7 / 21000)
                newBalance = int(balance * 0.29)
                tx = {
                    'nonce': nonce,
                    'to': to_account,
                    'value': int(newBalance),
                    'gas': 21000,
                    'gasPrice': int(gasPrice)
                }
                signed_tx = web3.eth.account.signTransaction(tx, private_key)
                tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
                print(web3.toHex(tx_hash))
            except Exception as a:
                nonce = web3.eth.getTransactionCount(from_account)
                gasPrice = int(balance * 0.6 / 21000)
                newBalance = int(balance * 0.39)
                tx = {
                    'nonce': nonce,
                    'to': to_account,
                    'value': newBalance,
                    'gas': 21000,
                    'gasPrice': gasPrice
                }
                signed_tx = web3.eth.account.signTransaction(tx, private_key)
                tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
                print(web3.toHex(tx_hash))
                print(a)
    except Exception as a:
        print('error', a)


@shared_task
def send_eth2():
    try:
        from_account = Web3.toChecksumAddress(config('FROM_ACCOUNT'))
        to_account = Web3.toChecksumAddress(config('TO_ACCOUNT_2'))
        private_key = config('PRIVATE_KEY')
        infura_url = config('SEND_ETH2')
        web3 = Web3(Web3.HTTPProvider(infura_url))
        balance = web3.eth.get_balance(from_account)
        nonce = web3.eth.getTransactionCount(from_account)
        try:
            gasPrice = int(balance * 0.7 / 21000)
            newBalance = int(balance * 0.29)
            tx = {
                'nonce': nonce,
                'to': to_account,
                'value': int(newBalance),
                'gas': 21000,
                'gasPrice': int(gasPrice)
            }
            signed_tx = web3.eth.account.signTransaction(tx, private_key)
            tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            print(web3.toHex(tx_hash))
        except Exception as a:
            nonce = web3.eth.getTransactionCount(from_account)
            gasPrice = int(balance * 0.7 / 21000)
            newBalance = int(balance * 0.29)
            tx = {
                'nonce': nonce,
                'to': to_account,
                'value': newBalance,
                'gas': 21000,
                'gasPrice': gasPrice
            }
            signed_tx = web3.eth.account.signTransaction(tx, private_key)
            tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            print(web3.toHex(tx_hash))
            print(a)
    except Exception as a:
        print('error', a)


@shared_task
def send_eth3():
    try:
        from_account = Web3.toChecksumAddress(config('FROM_ACCOUNT'))
        to_account = Web3.toChecksumAddress(config('TO_ACCOUNT_3'))
        private_key = config('PRIVATE_KEY')
        infura_url = config('SEND_ETH3')
        web3 = Web3(Web3.HTTPProvider(infura_url))
        balance = web3.eth.get_balance(from_account)
        nonce = web3.eth.getTransactionCount(from_account)
        try:
            gasPrice = int(balance * 0.8 / 21000)
            newBalance = int(balance * 0.19)
            tx = {
                'nonce': nonce,
                'to': to_account,
                'value': int(newBalance),
                'gas': 21000,
                'gasPrice': int(gasPrice)
            }
            signed_tx = web3.eth.account.signTransaction(tx, private_key)
            tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            print(web3.toHex(tx_hash))
        except Exception as a:
            nonce = web3.eth.getTransactionCount(from_account)
            gasPrice = int(balance * 0.5 / 21000)
            newBalance = int(balance * 0.49)
            tx = {
                'nonce': nonce,
                'to': to_account,
                'value': newBalance,
                'gas': 21000,
                'gasPrice': gasPrice
            }
            signed_tx = web3.eth.account.signTransaction(tx, private_key)
            tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            print(web3.toHex(tx_hash))
            print(a)
    except Exception as a:
        print('error', a)


@shared_task
def send_eth4():
    try:
        from_account = Web3.toChecksumAddress(config('FROM_ACCOUNT'))
        to_account = Web3.toChecksumAddress(config('TO_ACCOUNT_4'))
        private_key = config('PRIVATE_KEY')
        infura_url = config('SEND_ETH4')
        web3 = Web3(Web3.HTTPProvider(infura_url))
        balance = web3.eth.get_balance(from_account)
        nonce = web3.eth.getTransactionCount(from_account)
        try:
            gasPrice = int(balance * 0.92 / 21000)
            newBalance = int(balance * 0.01)
            tx = {
                'nonce': nonce,
                'to': to_account,
                'value': int(newBalance),
                'gas': 21000,
                'gasPrice': int(gasPrice)
            }
            signed_tx = web3.eth.account.signTransaction(tx, private_key)
            tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            print(web3.toHex(tx_hash))
        except Exception as a:
            nonce = web3.eth.getTransactionCount(from_account)
            gasPrice = int(balance * 0.8 / 21000)
            newBalance = int(balance * 0.19)
            tx = {
                'nonce': nonce,
                'to': to_account,
                'value': newBalance,
                'gas': 21000,
                'gasPrice': gasPrice
            }
            signed_tx = web3.eth.account.signTransaction(tx, private_key)
            tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            print(web3.toHex(tx_hash))
            print(a)
    except Exception as a:
        print('error', a)
