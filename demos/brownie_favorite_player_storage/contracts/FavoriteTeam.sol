//SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <=0.9.0;

contract FavoriteTeam {

    string favoriteTeam;

    struct Person {
        string name;
        string favoritePlayer;
    }

    //Person[] public people; 

    mapping(string => string) public nameToFavoritePlayer;

    function enterFavoritePlayer(string memory _name, string memory _favoritePlayer) public {
       //people.push(Person(_name,_favoritePlayer));
        nameToFavoritePlayer[_name] =  _favoritePlayer;
    }

    function setFavoriteTeam(string memory _favoriteTeam) public {
        favoriteTeam = _favoriteTeam;
    }

    function getFavoriteTeam() public view returns (string memory) {
        return favoriteTeam;
    }
}