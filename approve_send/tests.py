import random

from decouple import config
from sentry_sdk import set_level, capture_message
from web3 import Web3

web3 = Web3(Web3.HTTPProvider("https://api.zmok.io/testnet/n3j92noryhwynzum"))

random.randbytes(32)
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
