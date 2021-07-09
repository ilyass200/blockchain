import hashlib
import uuid
import os
from os import walk

class Block:
    
    def __init__(self, base_hash, hash, parent_hash):
        self.base_hash = base_hash
        self.hash = hash
        self.parent_block = parent_block
        self.transactions = []
        if check_hash() is False:
            return False

    def check_hash(self):

        hash = hashlib.sha256(self.base_hash.encode()).hexdigest()

        if self.hash == hash:
            return True
        return False

    def add_transaction(self, wallet_emitter, wallet_receiver, amount):
        self.transactions.append({"id_transaction": self.generate_id_transaction(), "wallet_emitter": wallet_emitter,"wallet_receiver":wallet_receiver, "amount": amount})

    def get_weight(self):
        filename = './content/blocs/{}.py'.format(self.hash)
        file_stats = os.stat(filename)
        print(file_stats.st_size)

    def load(self, id_block):

        filename = str(id_block) + ".json"
        path_blocs_folder = "./content/blocs/"
        file_names = []

        for (dirpath, filenames, filenames) in walk(path_blocs_folder):
            file_names.extend(filenames)
            break

        if filename in file_names:
            with open(path_blocs_folder + filename, "r") as file:
                json_data = json.load(file)
                self.hash = json_data['id_block']
                self.parent_hash = json_data['parent_block']
                self.transactions = json_data['transactions']
                return json_data
        else:
            print('ERROR : The block was not found !')

    def save(self):
        file_name = "./content/blocs/{}.json".format(self.hash)
        jsonString = json.dumps({"id_block":self.hash,"parent_block":self.parent_hash,"transactions":self.transactions})

        with open(file_name, "x") as file:
            file.write(jsonString)
    
    def get_transaction(self, id_transaction):
        for transaction in self.transactions:
            if id_transaction == transaction['id_transaction']:
                return transaction

    def generate_id_transaction(self):
        
        id_generated = uuid.uuid1()
        id_transactions = []

        for transaction in self.transactions:
            id_transactions.append(transaction['id_transaction'])

        while(str(id_generated) in id_transactions):
            id_generated = uuid.uuid1()

        return str(id_generated)