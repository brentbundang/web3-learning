// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {
    //Favorite number is initalized to 0
    uint256 favoriteNumber;
    // bool favoriteBool = true;
    // string favoriteString = "String";
    // int256 favoriteInt = -5;
    // address favoriteAddress = "";
    // bytes32 favoriteBytes = "cat";j

    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People[] public people;
    mapping(string => uint256) public nameToFavoriteNumbers;

    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
    }

    //Doesn't change the state just views and returns it
    function retrieve() public view returns (uint256) {
        return favoriteNumber;
    }

    //Pure functions for math based operations
    //function add(uint256 favorite) public pure {
    //  favorite + favorite;
    //}

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People(_favoriteNumber, _name));
        nameToFavoriteNumbers[_name] = _favoriteNumber;
    }
}
