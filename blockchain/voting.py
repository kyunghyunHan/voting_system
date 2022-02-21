from web3 import Web3
import json

with open("./build/contracts/Voting.json", 'r') as f:
		js = json.load(f)
		abi = js['abi']
		address = js['networks']['5777']['address'].upper()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:9545"))
w3.eth.defaultAccount = w3.eth.accounts[0]

adr = w3.toChecksumAddress(address)
voting = w3.eth.contract(address=adr,abi=abi)

# tx_hash = voting.functions.addElection(5,"테스트테스",123,456)
# tx_hash = tx_hash.transact()

tx_hash = voting.functions.addCandidate(4,"a","a",5)
tx_hash = tx_hash.transact()
# w3.eth.waitForTransactionReceipt(tx_hash)

election = voting.functions.getLastElection().call()

print(election)

