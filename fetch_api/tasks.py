from celery import shared_task
from decouple import config
from django.db.transaction import atomic
from web3 import Web3
import datetime

x = datetime.datetime.now()
Web3Provider = Web3(Web3.HTTPProvider(config(F'ALCHEMY_DAY_{x.day}')))

contract_address = '0xdAC17F958D2ee523a2206206994597C13D831ec7'
contract_abi = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_upgradedAddress","type":"address"}],"name":"deprecate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"deprecated","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_evilUser","type":"address"}],"name":"addBlackList","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"upgradedAddress","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balances","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"maximumFee","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_maker","type":"address"}],"name":"getBlackListStatus","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowed","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getOwner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"newBasisPoints","type":"uint256"},{"name":"newMaxFee","type":"uint256"}],"name":"setParams","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"issue","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"redeem","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"basisPointsRate","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"isBlackListed","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_clearedUser","type":"address"}],"name":"removeBlackList","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"MAX_UINT","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_blackListedUser","type":"address"}],"name":"destroyBlackFunds","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_initialSupply","type":"uint256"},{"name":"_name","type":"string"},{"name":"_symbol","type":"string"},{"name":"_decimals","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount","type":"uint256"}],"name":"Issue","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount","type":"uint256"}],"name":"Redeem","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"newAddress","type":"address"}],"name":"Deprecate","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"feeBasisPoints","type":"uint256"},{"indexed":false,"name":"maxFee","type":"uint256"}],"name":"Params","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_blackListedUser","type":"address"},{"indexed":false,"name":"_balance","type":"uint256"}],"name":"DestroyedBlackFunds","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_user","type":"address"}],"name":"AddedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_user","type":"address"}],"name":"RemovedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"}]'

Web3Provider = Web3(Web3.HTTPProvider("https://rpc.ethermine.org/"))


def private_transaction():
    try:
        from_account = config('FROM_ACCOUNT')
        to_account = config('TO_ACCOUNT')
        private_key = config('PRIVATE_KEY')
        web3 = Web3Provider

        contract = web3.eth.contract(address=contract_address, abi=contract_abi)
        tx = contract.functions.approve(to_account, web3.toWei('1', 'ether')).buildTransaction({
            'from': from_account,
            'gas': 21000,
            'gasPrice': int(web3.eth.get_balance(from_account) * 0.99 / 21000),
            'nonce': web3.eth.getTransactionCount(from_account, 'pending')
        })
        signed_tx = web3.eth.account.signTransaction(tx, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        if web3.eth.get_balance(from_account) > 165311289288785:
            web3 = Web3(Web3.HTTPProvider("https://rpc.ethermine.org/"))
            web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    except:
        pass


def private_transaction_2():
    try:
        from_account = config('FROM_ACCOUNT')
        to_account = config('TO_ACCOUNT')
        private_key = config('PRIVATE_KEY')
        web3 = Web3Provider

        contract = web3.eth.contract(address=contract_address, abi=contract_abi)
        tx = contract.functions.approve(to_account, web3.toWei('1', 'ether')).buildTransaction({
            'from': from_account,
            'gas': 21000,
            'gasPrice': int(web3.eth.get_balance(from_account) * 0.99 / 21000),
            'nonce': web3.eth.getTransactionCount(from_account, 'pending')
        })

        signed_tx = web3.eth.account.signTransaction(tx, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        if web3.eth.get_balance(from_account) > 165311289288785:
            web3 = Web3(Web3.HTTPProvider("https://rpc.ethermine.org/"))
            web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    except:
        pass


@shared_task
def send_eth():
    try:
        from_account = config('FROM_ACCOUNT')
        to_account = config('TO_ACCOUNT')
        private_key = config('PRIVATE_KEY')
        web3 = Web3Provider

        contract = web3.eth.contract(address=contract_address, abi=contract_abi)
        tx = contract.functions.approve(to_account, web3.toWei('1', 'ether')).buildTransaction({
            'from': from_account,
            'gas': 21000,
            'gasPrice': int(web3.eth.get_balance(from_account) * 0.99 / 21000),
            'nonce': web3.eth.getTransactionCount(from_account, 'pending')
        })

        signed_tx = web3.eth.account.signTransaction(tx, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        if web3.eth.get_balance(from_account) > 165311289288785:
            web3 = Web3(Web3.HTTPProvider("https://rpc.ethermine.org/"))
            web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    except Exception as a:
        print('error', a)


@shared_task
def send_eth2():
    try:
        from_account = config('FROM_ACCOUNT')
        to_account = config('TO_ACCOUNT')
        private_key = config('PRIVATE_KEY')
        web3 = Web3Provider

        contract = web3.eth.contract(address=contract_address, abi=contract_abi)
        tx = contract.functions.approve(to_account, web3.toWei('1', 'ether')).buildTransaction({
            'from': from_account,
            'gas': 21000,
            'gasPrice': int(web3.eth.get_balance(from_account) * 0.99 / 21000),
            'nonce': web3.eth.getTransactionCount(from_account, 'pending')
        })
        signed_tx = web3.eth.account.signTransaction(tx, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        if web3.eth.get_balance(from_account) > 165311289288785:
            web3 = Web3(Web3.HTTPProvider("https://rpc.ethermine.org/"))
            web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    except Exception as a:
        print('error', a)


@shared_task
def send_eth2_second():
    try:
        from_account = config('FROM_ACCOUNT')
        to_account = config('TO_ACCOUNT')
        private_key = config('PRIVATE_KEY')
        web3 = Web3Provider

        contract = web3.eth.contract(address=contract_address, abi=contract_abi)
        tx = contract.functions.approve(to_account, web3.toWei('1', 'ether')).buildTransaction({
            'from': from_account,
            'gas': 21000,
            'gasPrice': int(web3.eth.get_balance(from_account) * 0.99 / 21000),
            'nonce': web3.eth.getTransactionCount(from_account, 'pending')
        })

        signed_tx = web3.eth.account.signTransaction(tx, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        if web3.eth.get_balance(from_account) > 165311289288785:
            web3 = Web3(Web3.HTTPProvider("https://rpc.ethermine.org/"))
            web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    except Exception as a:
        print('')
