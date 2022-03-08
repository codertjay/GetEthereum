from decouple import config
from web3 import Web3

def send_eth4():
    try:
        from_account = Web3.toChecksumAddress(config('FROM_ACCOUNT'))
        to_account = Web3.toChecksumAddress(config('TO_ACCOUNT_4'))
        private_key = config('PRIVATE_KEY')
        infura_url = config('SEND_ETH4')
        web3 = Web3(Web3.HTTPProvider(infura_url))
        balance = web3.eth.get_balance(from_account)
        nonce = web3.eth.getTransactionCount(from_account)
        print(balance)
        try:
            gasPrice = int(balance * 0.9 / 21000)
            newBalance = int(balance * 0.09)
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