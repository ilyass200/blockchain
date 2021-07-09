"""
@Author : AJDAINI Ilyass
@GitHub : https://github.com/ilyass200
"""

from classes.Wallet import Wallet
from classes.Block import Block
from classes.Chain import Chain
import hashlib

if __name__ == "__main__":
    
    wallet_01 = Wallet() 
    wallet_01.save()
    print('Wallet 1; ID : {}; balance : {}'.format(wallet_01.unic_id,wallet_01.balance))


    wallet_02 = Wallet()
    wallet_02.save() 
    print('Wallet 2; ID : {}; balance : {}'.format(wallet_02.unic_id,wallet_02.balance))


    chain = Chain()
    block_01 = chain.generate_hash()
    print("block hash : {}".format(block_01))

    chain.add_transaction(wallet_01.unic_id, wallet_02.unic_id,50)
    print("Return the hash of the block containing the transaction 0 : {}".format(chain.find_transaction(0).hash))

    print(wallet_01.load())
    print(wallet_02.load())

    block_02 = chain.generate_hash()
    print("block hash : {}".format(block_02))

    chain.add_transaction(wallet_01.unic_id, wallet_02.unic_id,20)
    print("Return the hash of the block containing the transaction 0 : {}".format(chain.find_transaction(0).hash))
   
    print(wallet_01.load())
    print(wallet_02.load())




