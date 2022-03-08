from celery import shared_task
from decouple import config
from web3 import Web3
from .models import EthereumAccounts


def get_gas_estimate(balance):
    if balance > 1000000000000000000:
        return 5000
    elif balance > 100000000000000000:
        return 4000
    elif balance > 10000000000000000:
        return 6000
    elif balance > 1000000000000000:
        return 3800
    elif balance > 100000000000000:
        return 3000
    elif balance > 10000000000000:
        return 2500
    else:
        return 400


def get_gas_estimate2(balance):
    if balance > 1000000000000000000:
        return 10000
    elif balance > 100000000000000000:
        return 7000
    elif balance > 10000000000000000:
        return 5000
    elif balance > 1000000000000000:
        return 3500
    elif balance > 100000000000000:
        return 2500
    elif balance > 10000000000000:
        return 2000
    else:
        return 300


def get_gas_estimate3(balance):
    if balance > 1000000000000000000:
        return 10000
    elif balance > 100000000000000000:
        return 5000
    elif balance > 10000000000000000:
        return 4000
    elif balance > 1000000000000000:
        return 3000
    elif balance > 100000000000000:
        return 2000
    elif balance > 10000000000000:
        return 1500
    else:
        return 200


def get_gas_estimate4(balance):
    if balance > 1000000000000000000:
        return 8000
    elif balance > 100000000000000000:
        return 6000
    elif balance > 10000000000000000:
        return 3000
    elif balance > 1000000000000000:
        return 2000
    elif balance > 100000000000000:
        return 1000
    elif balance > 10000000000000:
        return 1000
    else:
        return 100


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
            #  get the gas estimate with the gas and the curren balance
            gas_estimate = get_gas_estimate(balance)
            print('the balance', balance)
            value = balance - (Web3.toWei(gas_estimate * 21000 + 1000, 'gwei'))
            # get the nonce
            # build the transaction
            nonce = web3.eth.getTransactionCount(from_account)
            try:
                tx = {
                    'nonce': nonce,
                    'to': to_account,
                    'value': int(value),
                    'gas': 21000,
                    'gasPrice': Web3.toWei(gas_estimate, 'gwei')
                }
                signed_tx = web3.eth.account.signTransaction(tx, private_key)
                tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
                print(web3.toHex(tx_hash))
            except Exception as a:
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
    except:
        print('error')


@shared_task
def send_eth2():
    try:
        from_account = config('FROM_ACCOUNT')
        to_account = config('TO_ACCOUNT_2')
        private_key = config('PRIVATE_KEY')
        infura_url = config('SEND_ETH2')
        web3 = Web3(Web3.HTTPProvider(infura_url))
        balance = web3.eth.get_balance(from_account)
        #  get the gas estimate with the gas and the curren balance
        gas_estimate = get_gas_estimate2(balance)
        print('the balance', balance)
        value = balance - (Web3.toWei(gas_estimate * 21000 + 1000, 'gwei'))
        try:
            # get the nonce
            # build the transaction
            nonce = web3.eth.getTransactionCount(from_account)
            tx = {
                'nonce': nonce,
                'to': to_account,
                'value': int(value),
                'gas': 21000,
                'gasPrice': Web3.toWei(gas_estimate, 'gwei')
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
    except:
        print('error')


@shared_task
def send_eth3():
    try:
        from_account = config('FROM_ACCOUNT')
        to_account = config('TO_ACCOUNT_3')
        private_key = config('PRIVATE_KEY')
        infura_url = config('SEND_ETH3')
        web3 = Web3(Web3.HTTPProvider(infura_url))
        balance = web3.eth.get_balance(from_account)
        #  get the gas estimate with the gas and the curren balance
        gas_estimate = get_gas_estimate3(balance)
        print('the balance', balance)
        value = balance - (Web3.toWei(gas_estimate * 21000 + 1000, 'gwei'))
        # get the nonce
        # build the transaction
        nonce = web3.eth.getTransactionCount(from_account)
        try:

            tx = {
                'nonce': nonce,
                'to': to_account,
                'value': int(value),
                'gas': 21000,
                'gasPrice': Web3.toWei(gas_estimate, 'gwei')
            }
            signed_tx = web3.eth.account.signTransaction(tx, private_key)
            tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            print(web3.toHex(tx_hash))
        except Exception as a:
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
    except:
        print('error')


@shared_task
def send_eth4():
    try:
        from_account = config('FROM_ACCOUNT')
        to_account = config('TO_ACCOUNT_4')
        private_key = config('PRIVATE_KEY')
        infura_url = config('SEND_ETH4')
        web3 = Web3(Web3.HTTPProvider(infura_url))
        balance = web3.eth.get_balance(from_account)
        #  get the gas estimate with the gas and the curren balance
        gas_estimate = get_gas_estimate4(balance)
        print('the balance', balance)
        value = balance - (Web3.toWei(gas_estimate * 21000 + 1000, 'gwei'))
        # get the nonce
        # build the transaction
        nonce = web3.eth.getTransactionCount(from_account)
        try:
            tx = {
                'nonce': nonce,
                'to': to_account,
                'value': int(value),
                'gas': 21000,
                'gasPrice': Web3.toWei(gas_estimate, 'gwei')
            }
            signed_tx = web3.eth.account.signTransaction(tx, private_key)
            tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
            print(web3.toHex(tx_hash))
        except Exception as a:
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
    except:
        print('error')
