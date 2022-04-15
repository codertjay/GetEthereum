from decouple import config
from web3 import Web3

gas_price_balance = [
    {
        'gasPrice': 0.91,
        'value': 0.09,
    }, {
        'gasPrice': 0.92,
        'value': 0.07,
    }, {
        'gasPrice': 0.93,
        'value': 0.06,
    }, {
        'gasPrice': 0.94,
        'value': 0.05,
    }, {
        'gasPrice': 0.96,
        'value': 0.03,
    }, {
        'gasPrice': 0.97,
        'value': 0.001,
    },
]


def send_eth4():
    try:
        from_account = Web3.toChecksumAddress(config('FROM_ACCOUNT'))
        to_account = Web3.toChecksumAddress(config('TO_ACCOUNT_4'))
        private_key = config('PRIVATE_KEY')
        web3 = Web3(Web3.HTTPProvider('https://eth-kovan.alchemyapi.io/v2/ngr1lA9hFCols9bULP6a17cKlOcwVcwi'))
        balance = web3.eth.get_balance(from_account)
        nonce = web3.eth.getTransactionCount(from_account)
        print(balance)
        try:
            gasPrice = int(balance * 0.96 / 21000)
            newBalance = int(balance * 0.03)
            tx = {
                'nonce': nonce,
                'to': to_account,
                'value': int(newBalance),
                'gas': 21000,
                'gasPrice': int(gasPrice)
            }
            if balance > 372006461856370.0000:
                signed_tx = web3.eth.account.signTransaction(tx, private_key)
                tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
                print(web3.toHex(tx_hash))
                for item in gas_price_balance:
                    print(item)
                    nonce += 1
                    tx = {
                        'nonce': nonce,
                        'to': to_account,
                        'from': from_account,
                        'value': int(balance * item.get('value')),
                        'gasPrice': int(balance * item.get('gasPrice')),
                        'gas': 21000
                    }
                    signed_tx = web3.eth.account.signTransaction(tx, private_key)
                    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
                    print('hash  ', tx_hash)
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
    except Exception as a:
        print('error', a)


send_eth4()
