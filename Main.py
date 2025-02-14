import os
from Chain import Chain

DIFFICULTY = 20
initial_data = {
    'Transaction1': 'A pays 4btc to B',
    'Transaction2': 'C pays 0.5btc to D',
    'Transaction3': 'E pays 3.34btc to F',
    'Transaction4': 'G pays 1btc to H',
    'Transaction5': 'I pays 2.3btc to J',
}

if not os.path.exists('BlockChain.json'):
    Chain.create_chain()

mined_successful = Chain.write_on_chain(initial_data, DIFFICULTY)
print('Mining Successful' if mined_successful else 'Mining Not Successful')

additional_data = {}
for count in range(2):
    data = input('Add Something on Chain: ')
    additional_data[count] = data

mined_successful = Chain.write_on_chain(additional_data, DIFFICULTY)
print('Mining Successful' if mined_successful else 'Mining Not Successful')
