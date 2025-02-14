import json
import hashlib
from Block import Block

class Chain:
    @staticmethod
    def create_chain():
        genesis_block_data = {
            'Block index': 0,
            'Block data': 'genesis',
            'Block hash': None,
            'Block nonce': None,
            'Previous hash': '0'
        }

        genesis_block = Block(0, genesis_block_data['Block data'])
        genesis_block.mine(genesis_block_data['Block data'], '0', 10)

        genesis_block_data['Block hash'] = genesis_block.hash
        genesis_block_data['Block nonce'] = genesis_block.nonce

        with open('BlockChain.json', 'w') as bc:
            json.dump([genesis_block_data], bc, indent=4)

        Block.update_latest_block('0', genesis_block)

    @staticmethod
    def write_on_chain(data, difficulty):
        with open('BlockChain.json', 'r+') as bc:
            chain = json.load(bc)
            latest_index, previous_hash = Block.get_latest_block()
            
            new_block = Block(latest_index + 1, data)
            new_block.mine(data, previous_hash, difficulty)

            if Chain.proof_of_work(data, previous_hash, difficulty, new_block):
                Block.update_latest_block(previous_hash, new_block)
                block_data = {
                    'Block index': new_block.index,
                    'Block data': data,
                    'Block hash': new_block.hash,
                    'Block nonce': new_block.nonce,
                    'Previous hash': previous_hash,
                }
                chain.append(block_data)

                bc.seek(0)
                json.dump(chain, bc, indent=4)
                bc.truncate()

                return True
            return False

    @staticmethod
    def proof_of_work(data, previous_hash, difficulty, block):
        nonce = block.nonce
        unmined_block = (str(data) + str(previous_hash) + str(nonce)).encode('utf-8')
        hash_result = hashlib.sha256(unmined_block).hexdigest()

        return int(hash_result, 16) < 2**(256 - difficulty)
