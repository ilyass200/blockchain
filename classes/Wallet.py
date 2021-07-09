
import uuid
import json
from os import walk

class Wallet:

    def __init__(self, unic_id=None):
        if unic_id is None:
            self.unic_id = self.generate_unique_id()
            self.balance = 100
            self.history = []
        else:
            self.unic_id = unic_id
            self.load()


    def generate_unique_id(self):
        
        file_names = []
        for (dirpath, s, filenames) in walk("./content/wallets"):
            file_names.extend(filenames)
            break

        unic_id = uuid.uuid1()

        # check if an identifier already exists in the wallet content
        while(str(unic_id) + ".json" in file_names):
            unic_id = uuid.uuid1()
        
        return str(unic_id)

    def add_balance(self, transaction):
        self.balance = self.balance + transaction["amount"]
        self.send(transaction)
    
    def sub_balance(self, transaction):
        if transaction["amount"] >= self.balance:
            print("ERROR : The amount is higher than your balance !")
        else:
            self.balance = self.balance - transaction["amount"] 
            self.send(transaction)

    def send(self, transaction):
        add_transaction = {
            "wallet_emitter": transaction['wallet_emitter'],
            "wallet_receiver": transaction['wallet_receiver'],
            "amount": transaction['amount']
        }
        self.history.append(add_transaction)
        self.save()

    def load(self):

        filename = str(self.unic_id) + ".json"
        path_wallets_folder = "./content/wallets/"
        file_names = []

        for (dirpath, filenames, filenames) in walk(path_wallets_folder):
            file_names.extend(filenames)
            break

        if filename in file_names:
            with open(path_wallets_folder + filename, "r") as file:
                json_data = json.load(file)
                self.unic_id = json_data['id']
                self.balance = json_data['balance']
                self.history = json_data['history']
                return json_data
        else:
            print('ERROR : The identification number was not found !')



    def save(self):
        file_name = "./content/wallets/{}.json".format(self.unic_id)
        jsonString = json.dumps({"id": self.unic_id,"balance": self.balance, "history": self.history})

        with open(file_name, "w") as file:
            file.write(jsonString)