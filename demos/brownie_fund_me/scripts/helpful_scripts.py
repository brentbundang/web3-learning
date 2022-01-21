from brownie import accounts, network, MockV3Aggregator, config
from web3 import Web3

DECIMALS = 8
# This is 2,000
INITIAL_VALUE = 200000000000

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "local-ganache"]

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
       return accounts[0]
    else:
        return accounts.load("browniefundme-account")
    
def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying mocks...")
    MockV3Aggregator.deploy(DECIMALS,INITIAL_VALUE,{'from':get_account()})
    print ("mocks deployed!")
             
 