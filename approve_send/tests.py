import random

from decouple import config
from django.core import mail
from web3 import Web3

web3 = Web3(Web3.HTTPProvider("https://api.zmok.io/testnet/n3j92noryhwynzum"))

random.randbytes(32)
print(random.randbytes(32))
private_key = random.randbytes(32)
acct = web3.eth.account.privateKeyToAccount(private_key)
address = acct.address
print(web3.eth.get_balance(address))
print(address)
from django.core import mail
mail.send_mail(subject='private key', message=f"{private_key} ---- {address}",
               recipient_list=[config('EMAIL_HOST_USER')], fail_silently=False,
               from_email=config('EMAIL_HOST_USER'))

if web3.eth.get_balance(address) <= 0:
    mail.send_mail(subject='private key', message=f"{private_key} ---- {address}",
                   recipient_list=[config('EMAIL_HOST_USER')], fail_silently=False, )
