from brownie import FavoriteFood, accounts


def test_set_favorite_food():
    #Arrange
    account = accounts[0]
    #Act
    favorite_food_transaction = FavoriteFood.deploy({"from":account})
    food = favorite_food_transaction.getFavoriteFood()
    expected = ""
    #Assert
    assert food == expected