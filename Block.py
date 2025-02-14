import hashlib
import json

class Block:
    def __init__(self, index, data):
        self.index = index
        self.data = data
        self.previous_hash = None
        self.hash = None
        self.nonce = 0

    def get_data(self):
        return self.index, self.data, self.hash, self.nonce

    def block_mined(self, hash_value, previous_hash, nonce):
        self.hash = hash_value
        self.previous_hash = previous_hash
        self.nonce = nonce

    def mine(self, data, previous_hash, difficulty):
        nonce = 0

        while True:
            unmined_block = (str(data) + str(previous_hash) + str(nonce)).encode('utf-8')
            hash_result = hashlib.sha256(unmined_block).hexdigest()
            if int(hash_result, 16) < 2**(256 - difficulty):
                self.block_mined(hash_result, previous_hash, nonce)
                break
            nonce += 1

    @staticmethod
    def update_latest_block(previous_hash, block):
        index, data, block_hash, block_nonce = block.get_data()
        block_info = {
            'Block index': index,
            'Block data': data,
            'Block hash': block_hash,
            'Block nonce': block_nonce,
            'Previous hash': previous_hash,
        }
        with open("LatestBlock.json", "w") as outfile:
            json.dump(block_info, outfile, indent=4)

    @staticmethod
    def get_latest_block():
        with open("LatestBlock.json", "r") as infile:
            data = json.load(infile)
            index = data["Block index"]
            previous_hash = data["Block hash"]
            return int(index), previous_hash
