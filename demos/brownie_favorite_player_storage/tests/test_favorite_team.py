from brownie import FavoriteTeam, accounts

def test_favorite_team():
    #Arrange
    account = accounts[0]
    #Act
    favorite_player = FavoriteTeam.deploy({"from":account})
    favorite_player.setFavoriteTeam("Memphis Grizzlies",{"from":account})
    favorite_team = favorite_player.getFavoriteTeam()
    expected = "Memphis Grizzlies"
    #Assert
    assert favorite_team == expected

def test_favorite_team_zero():
    #Arrange
    account = accounts[0]
    #Act
    favorite_team = FavoriteTeam.deploy({"from":account})
    team = favorite_team.getFavoriteTeam()
    expected = ''
    #Assert
    assert expected == team
