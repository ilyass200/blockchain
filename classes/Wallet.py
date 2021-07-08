
import uuid
import json
from os import walk

class Wallet:

    # init attributes
    unic_id = int
    balance = 0 # portfolio balance
    history = {} # transaction history

    def __init__(self):
        pass

    def generate_unique_id(self):
        
        file_names = []
        for (dirpath, s, filenames) in walk("./content/wallets"):
            file_names.extend(filenames)
            break

        unic_id = uuid.uuid1()

        # check if an identifier already exists in the wallet content
        while(str(unic_id) + ".json" in file_names):
            unic_id = uuid.uuid1()
        
        self.unic_id = int(unic_id)

    def add_balance(self, amount: int):
        self.balance = self.balance + amount
    
    def sub_balance(self, amount):
        if amount > self.balance:
            print("ERROR : The amount is higher than your balance !")
        else:
            self.balance = self.balance - amount 

    def send(self, unic_id):

        filename = str(unic_id) + ".json"
        path_wallets_folder = "./content/wallets/"
        file_names = []

        for (dirpath, s, filenames) in walk(path_wallets_folder):
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

        with open(file_name, "x") as file:
            file.write(jsonString)