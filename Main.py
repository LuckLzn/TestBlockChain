from telnetlib import DO
from Block import Block
import hashlib
import os.path
import json
from Chain import Chain
from array import array
Diff = 10
Data ={
    'Transaction1':'A pays 4btc to B',
    'Transaction2':'C pays 0.5btc to D',
    'Transaction3':'E pays 3.34btc to F',
    'Transaction4':'G pays 1btc to H',
    'Transaction5':'I pays 2.3btc to J',
}
if not os.path.exists('BlockChain.json'):
    Chain.CreateChain()
    
Try = Chain.WriteOnChain(Data, Diff)
if Try:
    print('Mining Seccesful')
else:
    print('Mining Not Succesful')
Data = {}
count = 0
print('Add Something on Chain:')
while(1):
    data = input()
    Data[count] = data
    count +=1
    if count == 2:
        break
        
Try =  Chain.WriteOnChain(Data, Diff)
if Try:
    print('Mining Seccesful')
else:
    print('Mining Not Succesful')
