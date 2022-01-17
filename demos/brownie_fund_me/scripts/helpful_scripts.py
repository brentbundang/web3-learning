from brownie import accounts, network


def get_account():
    if network.show_active() == "development":
       return accounts[0]
    else:
        return accounts.load("browniefundme-account")