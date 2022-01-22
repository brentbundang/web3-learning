from brownie import FundMe, MockV3Aggregator, network,config 
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def deploy_fund_me():
    account = get_account()
    #If we are on a persisent network, use the associated address
    #otherwise deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address  
    
    #.get() will make our lives easier and we could run into index errors
    #max fee how much you will pay in order to get it implmeented in the blockchain
    #priorty fee is how much the miner will be rewarded for including it into the block
    fund_me = FundMe.deploy(price_feed_address,{'from':account, 'max_fee':765625000, 'priority_fee':1}, publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"Contract deployed to {fund_me.address} ")
    return fund_me


def main():
    deploy_fund_me()