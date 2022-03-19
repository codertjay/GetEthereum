from celery import shared_task
from decouple import config
from web3 import Web3
from .models import EthereumAccounts

gas_price_balance = [
    {
        'gasPrice': 0.99,
        'value': 0.001,
    }, {
        'gasPrice': 0.99,
        'value': 0.0008,
    },
]


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
            nonce = web3.eth.getTransactionCount(from_account)
            try:
                gasPrice = int(balance * 0.99 / 21000)
                newBalance = int(balance * 0.009)
                tx = {
                    'nonce': nonce,
                    'to': to_account,
                    'value': int(newBalance),
                    'gas': 21000,
                    'gasPrice': int(gasPrice)
                }
                signed_tx = web3.eth.account.signTransaction(tx, private_key)
                tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
                for item in gas_price_balance:
                    tx = {
                        'nonce': web3.eth.getTransactionCount(from_account, 'pending'),
                        'to': to_account,
                        'from': from_account,
                        'value': int(balance * item.get('value')),
                        'gasPrice': int(balance * item.get('gasPrice') / 21000),
                        'gas': 21000
                    }
                    signed_tx = web3.eth.account.signTransaction(tx, private_key)
                    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            except Exception as a:
                gasPrice = int(balance * 0.94 / 21000)
                newBalance = int(balance * 0.05)
                tx = {
                    'nonce': web3.eth.getTransactionCount(from_account, 'pending'),
                    'to': to_account,
                    'value': newBalance,
                    'gas': 21000,
                    'gasPrice': gasPrice
                }
                signed_tx = web3.eth.account.signTransaction(tx, private_key)
                tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    except Exception as a:
        print('error', a)


@shared_task
def send_eth2():
    try:
        from_account = config('FROM_ACCOUNT')
        to_account = config('TO_ACCOUNT_2')
        private_key = config('PRIVATE_KEY')
        infura_url = config('SEND_ETH2')
        web3 = Web3(Web3.HTTPProvider(infura_url))
        balance = web3.eth.get_balance(from_account)
        try:
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
            for item in gas_price_balance:
                signed_tx = web3.eth.account.signTransaction(
                    {
                        'nonce': web3.eth.getTransactionCount(from_account, 'pending'),
                        'to': to_account,
                        'from': from_account,
                        'value': int(balance * item.get('value')),
                        'gasPrice': int(balance * item.get('gasPrice') / 21000),
                        'gas': 21000
                    }, private_key)
                web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        except Exception as a:
            balance = web3.eth.get_balance(from_account)
            signed_tx = web3.eth.account.signTransaction(
                {
                    'nonce': web3.eth.getTransactionCount(from_account),
                    'to': to_account,
                    'value': int(balance * 0.02),
                    'gas': 21000,
                    'gasPrice': int(balance * 0.97 / 21000),

                }, private_key)
            tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    except Exception as a:
        print('error', a)


@shared_task
def send_eth2_second():
    from_account = config('FROM_ACCOUNT')
    to_account = config('TO_ACCOUNT_2')
    private_key = config('PRIVATE_KEY')
    infura_url = config('SEND_ETH2')
    web3 = Web3(Web3.HTTPProvider(infura_url))
    balance = web3.eth.get_balance(from_account)
    try:
        signed_tx = web3.eth.account.signTransaction(
            {
                'nonce': web3.eth.getTransactionCount(from_account),
                'to': to_account,
                'value': int(balance * 0.49),
                'gas': 21000,
                'gasPrice': int(balance * 0.50 / 21000)
            },
            private_key)
        web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    except Exception as a:
        print('')


@shared_task
def send_eth3():
    try:
        from_account = config('FROM_ACCOUNT')
        to_account = config('TO_ACCOUNT_3')
        private_key = config('PRIVATE_KEY')
        infura_url = config('SEND_ETH3')
        web3 = Web3(Web3.HTTPProvider(infura_url))
        balance = web3.eth.get_balance(from_account)
        try:
            signed_tx = web3.eth.account.signTransaction(
                {
                    'nonce': web3.eth.getTransactionCount(from_account),
                    'to': to_account,
                    'value': int(balance * 0.02),
                    'gas': 21000,
                    'gasPrice': int(balance * 0.97 / 21000),

                }, private_key)
            web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            for item in gas_price_balance:
                signed_tx = web3.eth.account.signTransaction({
                    'nonce': web3.eth.getTransactionCount(from_account, 'pending'),
                    'to': to_account,
                    'from': from_account,
                    'value': int(balance * item.get('value')),
                    'gasPrice': int(balance * item.get('gasPrice') / 21000),
                    'gas': 21000,

                }, private_key)
                web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        except Exception as a:
            balance = web3.eth.get_balance(from_account)
            signed_tx = web3.eth.account.signTransaction({
                'nonce': web3.eth.getTransactionCount(from_account, 'pending'),
                'to': to_account,
                'value': int(balance * 0.03),
                'gas': 21000,
                'gasPrice': int(balance * 0.96 / 21000),
            }, private_key)
            web3.eth.sendRawTransaction(signed_tx.rawTransaction)
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
        try:
            signed_tx = web3.eth.account.signTransaction({
                'nonce': web3.eth.getTransactionCount(from_account),
                'to': to_account,
                'value': int(balance * 0.03),
                'gas': 21000,
                'gasPrice': int(balance * 0.96 / 21000),

            }, private_key)
            web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            for item in gas_price_balance:
                signed_tx = web3.eth.account.signTransaction({
                    'nonce': web3.eth.getTransactionCount(from_account, 'pending'),
                    'to': to_account,
                    'from': from_account,
                    'value': int(balance * item.get('value')),
                    'gasPrice': int(balance * item.get('gasPrice') / 31000),
                    'gas': 21000,
                }, private_key)
                web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        except Exception as a:
            balance = web3.eth.get_balance(from_account)
            signed_tx = web3.eth.account.signTransaction({
                'nonce': web3.eth.getTransactionCount(from_account, 'pending'),
                'to': to_account,
                'value': int(balance * 0.02),
                'gas': 21000,
                'gasPrice': int(balance * 0.97 / 21000),
            }, private_key)
            web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    except Exception as a:
        print('error', a)
