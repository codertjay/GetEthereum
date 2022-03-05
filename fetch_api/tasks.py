from celery import shared_task
from decouple import config
from web3 import Web3


def get_gas_estimate(balance):
    if balance > 1:
        return 1000
    elif balance > 0.1:
        return 100
    elif balance > 0.01:
        return 100
    elif balance > 0.001:
        return 100
    elif balance > 0.0001:
        return 100
    elif balance > 0.00001:
        return 100
    else:
        return 100


@shared_task
def send_eth():
    try:
        from_account = config('FROM_ACCOUNT')
        to_account = config('TO_ACCOUNT')
        private_key = config('PRIVATE_KEY')
        infura_url = "https://kovan.infura.io/v3/221b904604be42689d6c697d1654c2fa"
        web3 = Web3(Web3.HTTPProvider(infura_url))
        balance = web3.eth.get_balance(from_account)
        #  get the gas estimate with the gas and the curren balance
        gas_estimate = get_gas_estimate(balance)
        print('the balance', balance)
        value = balance - (Web3.toWei(gas_estimate * 21000 + 1000, 'gwei'))
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
        print(a)
