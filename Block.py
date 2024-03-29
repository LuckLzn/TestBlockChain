import hashlib
import json
class Block:
    def __init__(self, index, Data):
        self.index = index
        self.Data = Data
        self.Previous_Hash = None
        self.Hash = None
        self.Nounce = 0
        pass
    def getData(self):
        return self.index, self.Data, self.Hash, self.Nounce
    
    def BlockMined(self, Hash, Previous_Hash, Nounce):
        self.Hash = Hash
        self.Previous_Hash = Previous_Hash
        self.Nounce = Nounce
    
    def mine(self, Data, PrHash, Diff):
        nounce = 0
        umbhash = hashlib.sha256()

        while True:
            unminedblock = (str(Data) + str(PrHash) + str(nounce)).encode('utf-8')
            umbhash.update(unminedblock)
            hash_result = umbhash.hexdigest()
            if int(hash_result, 16) < 2**(256 - Diff):
                break
            umbhash = hashlib.sha256()  # Create a new hash object for the next iteration
            unminedblock = (str(Data) + str(PrHash) + str(nounce)).encode()
            nounce += 1

        
        self.BlockMined(hash_result, PrHash, nounce)
    
    @staticmethod
    def updateLatestblock(prhash, block):
        index, data, bhash, bnounce = Block.getData(block)
        dictionary ={
            'Block index' : index,
            'Block Data' : data,
            'Block Hash' : bhash,
            'Block Nounce' : bnounce,
            'Previous Hash' : prhash,
        }
        json_object = json.dumps(dictionary, indent = 4)
    
        # Writing to sample.json
        with open("LatestBlock.json", "w") as outfile:
            outfile.write(json_object)
   
    @staticmethod
    def getlatestBlock():
        with open("LatestBlock.json", "r") as outfile:
            data = json.load(outfile)
            index = data["Block index"]
            prhash = data["Block Hash"]
            return int(index), prhash