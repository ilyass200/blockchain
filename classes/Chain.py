from os import walk
import os
from classes.Block import Block
from classes.Wallet import Wallet
import hashlib
import sys

class Chain:


    def __init__(self):
        self.blocks = []
        self.last_transaction_number = 0

    def add_block(self, base_hash, hash):

        if len(self.blocks) < 1:
            parent_hash = "00"
        else:
            parent_hash = self.blocks[-1].hash

        block = Block(base_hash, hash, parent_hash)

        if block is not False:
            block.save()
            self.blocks.append(block)
        else:
            print('The hash of your string does not match with the given hash !')
    
    def get_block(self, hash):
        for block in self.blocks:
            if hash in block.hash:
                return self.blocks[block]
        print("No block has been found in the chain !")
        return False

    def add_transaction(self,emitter,receiver,amount):

        last_block = self.blocks[-1]
        wallet_emitter = Wallet(emitter)

        transaction = {"number": self.last_transaction_number,"wallet_emitter": emitter,"wallet_receiver":receiver,"amount": amount}

        if sys.getsizeof(transaction) + last_block.get_weight() < 250000:
            if wallet_emitter.balance >= amount:
                wallet_receiver = Wallet(receiver)
                self.last_transaction_number += 1
                wallet_emitter.sub_balance(transaction)
                wallet_receiver.add_balance(transaction)
                last_block.add_transaction(transaction)

        else:
            print('impossible to complete the transaction! the block has exceeded its limit of 250 000 bytes')


    def generate_hash(self):
        number = 0
        if len(self.blocks) < 1:
            parent_hash = "00"
        else:
            parent_hash = self.blocks[-1].hash
        
        block_hash = hashlib.sha256(f'{self.get_last_transaction_number()}{parent_hash}{number}'.encode()).hexdigest()

        while not self.verify_hash(block_hash):
            number = number + 1
            block_hash = hashlib.sha256(f'{self.get_last_transaction_number()}{parent_hash}{number}'.encode()).hexdigest()
        
        self.add_block(f'{self.get_last_transaction_number()}{parent_hash}{number}',block_hash)
        return block_hash

    def get_last_transaction_number(self):
        return self.last_transaction_number

    def find_transaction(self, transaction_number):
        for b in self.blocks:
            for t in b.transactions:
                if t['number'] == transaction_number:
                    return b
        return None

    def verify_hash(self, hash):
        filename = str(hash) + ".json"
        path_blocs_folder = "./content/blocs/"
        file_names = []

        for (dirpath, filenames, filenames) in walk(path_blocs_folder):
            file_names.extend(filenames)
            break

        if filename not in file_names and hash.startswith("0000"):
            return True
        else:
            return False
