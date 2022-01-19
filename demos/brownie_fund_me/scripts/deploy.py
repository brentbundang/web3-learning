from brownie import FundMe, MockV3Aggregator, network,config 
from scripts.helpful_scripts import get_account
from web3 import Web3

def deploy_fund_me():
    account = get_account()
    #If we are on a persisent network, use the associated address
    #otherwise deploy mocks
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        print(f"The active network is {network.show_active()}")
        print("Deploying mocks")
        mock_aggregator = MockV3Aggregator.deploy(18,Web3.toWei(2000,"ether"),{'from':account})
        price_feed_address = mock_aggregator.address 
    
    fund_me = FundMe.deploy(price_feed_address,{'from':account}, publish_source=config["networks"][network.show_active()].get(["verify"]))
    print(f"Contract deployed to {fund_me.address} ")
     
def main():
    deploy_fund_me()