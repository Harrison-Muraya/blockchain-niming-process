from time import time, sleep
import json
import hashlib

class Blockchain(object):
    def __init__(self):
        # self.chain = []
        self.chain = [self.addGenesisBlock()]
        self.pendingTranction = []
        self.difficulty = 2
        self.blockSize = 10
        self.minerReward =10


    def mineTransaction(self):
        lenPT = len(self.pendingTranction)

        for i in range (0, lenPT, self.blockSize):
            end = i + self.blockSize
            if i >= lenPT:
                end = lenPT
            transactionSlice = self.pendingTranction[i:end]
            newBlock = Block(transactionSlice, time(), len(self.chain))
            hashVal = self.getLastBlock().hash
            newBlock.prev = hashVal
            newBlock.mineBlock(self.difficulty)
            self.chain.append(newBlock)
        print('mining block transaction seccessiful')
    
    def mineBlock(self, difficulty):
        arr = []
        for i in range (0, difficulty):
            arr.append(1)
        
        arrStr = map(str, arr)
        hashPazzle = ''.join(arrStr)
        while self.hash[0:difficulty] != hashPazzle:
            self.nonse += 1
            self.hash = self.calculateHash()
            print('nonse: ', self.nonse)
            print('Hash Attempt: ', self.hash)
            print('hash we want: ', hashPazzle, '----' )
            print('')
            sleep(0.8)
            print("")
        print(' Block mined ! nonse to prove of work: ', self.nonse)
        return True

    def getLastBlock(self):
        return self.chain[-1]
    
    def addBlock(self, block):
        if(len(self.chain) > 0):
            block.prev = self.getLastBlock().hash
        else:
            block.prev = 'none'
        self.chain.append(block)

    def addGenesisBlock(self):
        tArry = []
        tArry.append(Transaction('harrison', '12:00 am', 100,time()))
        genesis = Block(tArry, time(), 0)
        genesis.prev = 'none'
        return genesis 

    # def chainJSONencode(self):
    #     chain_data = []
    #     for block in self.chain:
    #         chain_data.append(block.__dict__)
    #     return chain_data

    
class Block(object):
    def __init__(self, transactions, time, height):
        self.height = height
        self.time = time
        self.nonse = 0
        self.transactions = transactions
        self.prev = ''
        self.hash = self.calculateHash()
        

    def mineBlock(self, difficulty):
        arr = []
        for i in range(0, difficulty):
            arr.append(i)

        #compute until the beginning of the hash = 0123..difficulty
        arrStr = map(str, arr);  
        hashPuzzle = ''.join(arrStr)
        print(len(hashPuzzle))
        while self.hash[0:difficulty] != hashPuzzle:
            self.nonse += 1
            self.hash = self.calculateHash()

            print('nonse: ', self.nonse)
            print('Hash Attempt: ', self.hash)
            print('hash we want: ', hashPuzzle, '----' )
            print('')
            sleep(0.8)
            print("")

            # print(len(hashPuzzle))
            # print(self.hash[0:difficulty])
        print("Block Mined!")
        return True

    def calculateHash(self):
        hashTransactions = ''
        for transaction in self.transactions:
            hashTransactions += transaction.hash
        hashString = str(self.time) + hashTransactions + self.prev + str(self.height)
        hashEncoded = json.dumps(hashString, sort_keys=True).encode()
        return hashlib.sha256(hashEncoded).hexdigest()

class Transaction(object):
    def __init__(self, sender, receiver, amt, time):
        self.time = time
        self.sender = sender
        self.receiver = receiver
        self.amt = amt
        self.hash = self.calculateHash()

    def calculateHash(self):
        hashString = self.sender  + self.receiver + str(self.time) + str(self.amt)
        hashEncoded = json.dumps(hashString, sort_keys=True).encode()
        return hashlib.sha256(hashEncoded).hexdigest()