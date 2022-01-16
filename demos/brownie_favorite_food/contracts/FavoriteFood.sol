// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <=0.9.0;

contract FavoriteFood {

    string favoriteFood;

    //Get the favorite food
    function getFavoriteFood() public view returns (string memory) {
        return favoriteFood;
    }

    //Set the favorite food 
    function setFavoriteFood(string memory _favoriteFood) public {
        favoriteFood = _favoriteFood;
    }

}

