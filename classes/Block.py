import hashlib
import uuid
import json
import os
from os import walk

class Block:

    def __init__(self, base_hash, hash, parent_hash):
        self.base_hash = base_hash
        self.hash = hash
        self.parent_hash = parent_hash
        self.transactions = []
        if self.check_hash() is False:
            return False

    def check_hash(self):

        hash = hashlib.sha256(self.base_hash.encode()).hexdigest()

        if self.hash == hash:
            return True
        return False

    def add_transaction(self, transaction):
        self.transactions.append({"number": transaction['number'], "wallet_emitter": transaction["wallet_emitter"],"wallet_receiver":transaction["wallet_receiver"], "amount": transaction["amount"]})
        self.save()

    def get_weight(self):
        filename = './content/blocs/{}.json'.format(self.hash)
        file_stats = os.stat(filename)
        return file_stats.st_size

    def load(self, hash):

        filename = str(hash) + ".json"
        path_blocs_folder = "./content/blocs/"
        file_names = []

        for (dirpath, filenames, filenames) in walk(path_blocs_folder):
            file_names.extend(filenames)
            break

        if filename in file_names:
            with open(path_blocs_folder + filename, "r") as file:
                json_data = json.load(file)
                self.hash = json_data['hash']
                self.parent_hash = json_data['parent_hash']
                self.transactions = json_data['transactions']
                return json_data
        else:
            print('ERROR : The block was not found !')

    def save(self):
        file_name = "./content/blocs/{}.json".format(self.hash)
        jsonString = json.dumps({"hash":self.hash,"parent_hash":self.parent_hash,"transactions":self.transactions})

        with open(file_name, "w") as file:
            file.write(jsonString)
    
    def get_transaction(self, id_transaction):
        for transaction in self.transactions:
            if id_transaction == transaction['number']:
                return transaction