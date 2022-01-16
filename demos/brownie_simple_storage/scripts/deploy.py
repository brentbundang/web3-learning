from brownie import accounts, config


#Provides the ability to get an account from the 10 auto generated
#Sets the address, private key
def deploy_simple_storage():
    account = accounts[0] 
    #account = accounts.load("freecodecamp-account")
    #print(account)
    #account = accounts.add(config["wallets"]["from_key"])
    print(account)

def main():
    print("Hello!")
    deploy_simple_storage()