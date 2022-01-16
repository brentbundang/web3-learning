from brownie import accounts, FavoriteFood, network

def deploy_contract():
    account = get_account()
    favoriteFood = FavoriteFood.deploy({"from":account})
    transaction = favoriteFood.setFavoriteFood("Chicken", {"from":account})
    transaction.wait(1)
    print(favoriteFood.getFavoriteFood())
    
    
def get_account():
    if network.show_active()=="development":
        return accounts[0]
    else:
        return accounts.load("favoritefood-account")


def main():
    deploy_contract()