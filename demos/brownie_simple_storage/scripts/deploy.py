from brownie import accounts, config, SimpleStorage

#Provides the ability to get an account from the 10 auto generated
#Sets the address, private key
def deploy_simple_storage():
    account = accounts[0] 
    simple_storage = SimpleStorage.deploy({"from": account}) #Brownie is smart enough to know if it's a transaction or a call
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from":account})
    transaction.wait(1)
    updated_store_value = simple_storage.retrieve({"from":account})
    print(updated_store_value)

def main():
    print("Hello!")
    deploy_simple_storage()