from unittest.mock import Mock
from brownie import FundMe, MockV3Aggregator, network,config 
from scripts.helpful_scripts import get_account, deploy_mocks


def deploy_fund_me():
    account = get_account()
    #If we are on a persisent network, use the associated address
    #otherwise deploy mocks
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address  
    
    #.get() will make our lives easier and we could run into index errors
    fund_me = FundMe.deploy(price_feed_address,{'from':account}, publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"Contract deployed to {fund_me.address} ")
     
def main():
    deploy_fund_me()