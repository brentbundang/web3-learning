from brownie import FavoriteTeam, accounts, network

def deploy_contract():
   account = get_account()
   favorite_player = FavoriteTeam.deploy({"from":account})
   transaction = favorite_player.setFavoriteTeam("Memphis Grizzlies", ({"from":account}))
   transaction.wait(1)
   print(favorite_player.getFavoriteTeam())


def get_account():
    if network.show_active()=="development":
        return accounts[0]
    else:
        return accounts.load("favoriteplayer-account")
    
    
def main():
    deploy_contract()