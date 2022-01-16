from brownie import accounts, config, SimpleStorage, network

#Provides the ability to get an account from the 10 auto generated
#Sets the address, private key
#Dev networks is not persistent (brownie network list) 

def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account}) #Brownie is smart enough to know if it's a transaction or a call
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from":account})
    transaction.wait(1)
    updated_store_value = simple_storage.retrieve({"from":account})
    print(updated_store_value)


def get_account(): 
    if(network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    print("Hello!")
    deploy_simple_storage()