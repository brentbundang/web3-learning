//SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <=0.9.0;
pragma experimental ABIEncoderV2;

contract FavoriteMovies {

    struct Person {
        string name;
        uint256 rating;
        string nameOfMovie;
    }

    Person[] contestants;

    mapping(string => string) public nameToMovie;


    //NOTE: Memory is only needed for string, array, struct, or mappings and not uint. Uint is passed by value, the others are passed by reference
    function addContestant(string memory _contestant, uint256 _rating, string memory _nameOfMovie) public {
        contestants.push(Person(_contestant, _rating, _nameOfMovie));
    }
    
    //NOTE: In order to return struct ABIEncoder must be imported at the top of the file first 
    function retrieve(uint256 index) public view returns (Person memory p1){
        return contestants[index];
    }



}