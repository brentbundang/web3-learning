from brownie import accounts, network, MockV3Aggregator, config
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "local-ganache"]

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
       return accounts[0]
    else:
        return accounts.load("browniefundme-account")
    
def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying mocks...")
    if len(MockV3Aggregator) <=0:
        MockV3Aggregator.deploy(DECIMALS,Web3.toWei(STARTING_PRICE,"ether"),{'from':get_account()})
        print ("mocks deployed!")
             
 