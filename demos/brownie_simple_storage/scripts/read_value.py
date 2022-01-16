#Read from a contract that was already deployed on the blockchain 
from brownie import SimpleStorage, accounts, config 

def read_contract():
    simple_storage = SimpleStorage[-1] #Get the latest deployment
    #whenever interacting with the contact, we need the address and the ABI
    #The contract address is saved in the deployments rinkeby json 
    #we now have the address, and brownie knows its ABI after compiling it in build/contracts
    print(simple_storage.retrieve())
    pass

def main():
    read_contract()