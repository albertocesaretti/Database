import hashlib
import datetime
import json

class Block:
    def __init__(self, index, timestamp, transactions, digital_assets, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.digital_assets = digital_assets  # Lista di asset digitali nel blocco
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            'index': self.index,
            'timestamp': str(self.timestamp),
            'transactions': self.transactions,
            'digital_assets': self.digital_assets,
            'previous_hash': self.previous_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), [], [], "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def add_transaction(self, sender, receiver, amount):
        self.get_latest_block().transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })

    def create_digital_asset(self, owner, name, properties=None):
        asset = {
            'owner': owner,
            'name': name,
            'properties': properties if properties else {}
        }
        self.get_latest_block().digital_assets.append({'action': 'create', 'asset': asset})

    def transfer_digital_asset(self, asset_name, from_owner, to_owner):
        self.get_latest_block().digital_assets.append({
            'action': 'transfer',
            'asset_name': asset_name,
            'from': from_owner,
            'to': to_owner
        })

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False
        return True

# Creazione della blockchain
my_blockchain = Blockchain()
print("**************************")
# Aggiunta di transazioni
my_blockchain.add_transaction("Alice", "Bob", 10)
my_blockchain.add_transaction("Charlie", "David", 5)

# Creazione di asset digitali
my_blockchain.create_digital_asset("Alice", "Digital Art 1", {"artist": "Picasso"})
my_blockchain.create_digital_asset("Bob", "Collectible Card A", {"rarity": "Rare"})

# Trasferimento di un asset digitale
my_blockchain.transfer_digital_asset("Digital Art 1", "Alice", "Bob")

# Aggiunta di un nuovo blocco contenente le operazioni
new_block = Block(len(my_blockchain.chain), datetime.datetime.now(), my_blockchain.get_latest_block().transactions, my_blockchain.get_latest_block().digital_assets, my_blockchain.get_latest_block().hash)
my_blockchain.add_block(new_block)

# Aggiunta di altre transazioni e creazione di asset nel blocco successivo
my_blockchain.add_transaction("Eve", "Frank", 2)
my_blockchain.create_digital_asset("Charlie", "Virtual Land", {"size": "100 sq m"})
new_block_2 = Block(len(my_blockchain.chain), datetime.datetime.now(), [{'sender': 'Eve', 'receiver': 'Frank', 'amount': 2}], [{'action': 'create', 'asset': {'owner': 'Charlie', 'name': 'Virtual Land', 'properties': {'size': '100 sq m'}}}], my_blockchain.get_latest_block().hash)
my_blockchain.add_block(new_block_2)


# Stampa della blockchain (semplificata)
for block in my_blockchain.chain:
    print(f"Indice: {block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Transazioni: {block.transactions}")
    print(f"Asset Digitali: {block.digital_assets}")
    print(f"Hash: {block.hash}")
    print(f"Hash Precedente: {block.previous_hash}")
    print("-" * 30)

# Verifica della validità della blockchain
print(f"La blockchain è valida? {my_blockchain.is_chain_valid()}")


