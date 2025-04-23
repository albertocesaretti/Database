import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, transactions, previous_hash):
        self.index = index
        self.timestamp = timestamp #marca temporale
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index) + str(self.timestamp) + str(self.transactions) + str(self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                #print("numero blocco", i)
                #print("hash_blocco_corrente", current_block.hash)
                #print("hash_calcolato_blocco_corrente", current_block.calculate_hash())
                return False

            if current_block.previous_hash != previous_block.hash:
                return False
        return True

#main
# Esempio di utilizzo
mia_blockchain = Blockchain()

# Aggiungiamo delle transazioni (semplificate)
mia_blockchain.add_block(Block(1, datetime.datetime.now(), {"sender": "Alice", "receiver": "Bob", "amount": 10}, ""))
mia_blockchain.add_block(Block(2, datetime.datetime.now(), {"sender": "Charlie", "receiver": "David", "amount": 5}, ""))
mia_blockchain.add_block(Block(3, datetime.datetime.now(), {"sender": "Alberto", "receiver": "Roberto", "amount": 1500}, ""))
# Stampiamo la blockchain
for block in mia_blockchain.chain:
    print("Index:", block.index)
    print("Timestamp:", block.timestamp) # marca temporale
    print("Transactions:", block.transactions)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print("---")

# Verifichiamo se la catena è valida
print("Is chain valid?", mia_blockchain.is_chain_valid())


"""
# Tentiamo di manomettere un blocco (non funzionerà se la validazione è corretta)
mia_blockchain.chain[1].transactions = {"sender": "Eva", "receiver": "Luigi", "amount": 1000}
print("Is chain valid after tampering?", mia_blockchain.is_chain_valid())


# Stampiamo la blockchain
for block in mia_blockchain.chain:
    print("Index:", block.index)
    print("Timestamp:", block.timestamp) # marca temporale
    print("Transactions:", block.transactions)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print("---")
"""


