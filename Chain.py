from Block import Block
import json
import hashlib
class Chain:
    @staticmethod
    def CreateChain():
        chain = []
        Diff = 10
        f = open('BlockChain.json', 'w')
        obj = []
        json.dump(obj, f, indent = 4)
        f.close()
        with open('BlockChain.json') as Bc:
            chain = json.load(Bc)
            prevbl = 'genesis'
            genesis = Block('0', prevbl)
            genesis.mine(prevbl, '0', Diff)
            block = {
                'Block0' :{
                    'Block Index' : '0',
                    'Block Data': prevbl,
                    'Block Hash': genesis.Hash,
                    'Block Nounce': genesis.Nounce,
                    'Previous Hash': genesis.Previous_Hash,
                },
            }
            chain.append(block)
            Bc.close()
        with open ('BlockChain.json', 'w') as bc:
            json.dump(chain, bc, indent = 4, separators=(',', ': '))
            bc.close()
        Block.updateLatestblock('0', genesis)
    
    @staticmethod
    def WriteOnChain(Data, Diff):
        chain = []
        with open ('BlockChain.json', 'r') as bc:
            chain = json.load(bc)
            i, prev = Block.getlatestBlock()
            block = Block((i+1), Data)
            block.mine(Data, prev, Diff)
            if Chain.ProofofWork(Data, prev, Diff, block):
                Block.updateLatestblock(prev, block)
                indexb = i+1
                blocki = 'Block' + str(indexb)
                blockn = {
                    blocki : {
                        'Block Index' : indexb,
                        'Block Data': Data,
                        'Block Hash': block.Hash,
                        'Block Nounce': block.Nounce,
                        'Previous Hash':block.Previous_Hash,
                    },
                }
                chain.append(blockn)
                bc.close()
                with open ('BlockChain.json', 'w') as bc:  
                    json.dump(chain, bc, indent = 4)
                return True
            else:
                return False
    @staticmethod
    def ProofofWork(Data, prvH, Diff, block):
        i, bldata, Hash, Nounce = Block.getData(block)
        nounce = 0
        unminedblock = (str(Data) + str(prvH) + str(nounce)).encode()
        umbhash = hashlib.sha256()
        while(1):
            umbhash.update(unminedblock)
            hash = umbhash.hexdigest()
            if int(hash, 16) < 2**(256 - Diff):
                break
            unminedblock = (str(Data) + str(prvH) + str(nounce)).encode()
            nounce += 1
        if hash == Hash:
            return True