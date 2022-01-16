u

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)
    
#Get the byte code to deploy the file 
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# get abi
abi = json.loads(
    compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["metadata"]
)["output"]["abi"]


#Connect to the RPC  -- connecting to ganche (our local testing blockchain)
w3  = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/18f7a4be2460441ea0eaaff5155cd2a8"))
chain_id = 4
my_address = "0x92b3990826a5eB32ee31BFA88F076aEdF667177F"
#Add a 0x after adding the private key as you must prepend it to the private key -- python inclusive
private_key = os.getenv("PRIVATE_KEY")

#Create a contract
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

#Get the latest transaction in order to set the nonce 
nonce = w3.eth.getTransactionCount(my_address)

# 1. Build a transaction
# 2. Sign a transaction
# 3. Send a transaction

#Build the transaction
transaction = SimpleStorage.constructor().buildTransaction({"chainId":chain_id, "from":my_address, "nonce":nonce, "gasPrice": w3.eth.gas_price})

#Sign the transaction 
signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)

print("Deploying contract..")

#Send the transaction
tx_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)

#Wait for block confirmations -- good practice 
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

#Working with the contract
#Contract address
#Contract abi

print("Deployed!")


simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

# Interacting with a smart contract 
#Call -- > making the call and getting a return value (don't make a state change to the block chain) blue buttons in remix
#Transact -- > make a state change (yellow buttons in remix)




#A nonce can only be used once per each transaction
#Build
store_transaction = simple_storage.functions.store(15).buildTransaction({"chainId":chain_id, "from":my_address, "nonce":nonce+1, "gasPrice": w3.eth.gas_price})

#Sign
signed_store_txn = w3.eth.account.sign_transaction(store_transaction,private_key=private_key)

#Send
send_store_tx = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction) 
tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_tx)

print("Updated contract..")

#Initial value of our favorite number 
print(simple_storage.functions.retrieve().call())
