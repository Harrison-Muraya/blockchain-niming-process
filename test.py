from blockchain import *
from time import time
import pprint

pp = pprint.PrettyPrinter(indent = 4)

blockchain = Blockchain()
transaction = Transaction('harrison', 'muraya hh', 100, time())
blockchain.pendingTranction.append(transaction)

blockchain.mineTransaction()

# block = Block(transaction, time() , 1)
# blockchain.addBlock(block)

# block = Block(transaction, time() , 2)
# blockchain.addBlock(block)

# block = Block(transaction, time() , 3)
# blockchain.addBlock(block)

pp.pprint([block.__dict__ for block in blockchain.chain])


# pp.pprint(blockchain.chainJSONencode())
print('Lenght: ', len(blockchain.chain))