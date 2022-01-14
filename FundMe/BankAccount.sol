// SPDX-License-Identifier: MIT 

pragma solidity >=0.6.0 <0.9.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract BankAccount{
    address owner;
    mapping(address=>uint256) addressToAmount;
    AggregatorV3Interface internal priceFeed;

    constructor(){
        owner = msg.sender;
        priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
    }

    function deposit() public payable {
        addressToAmount[msg.sender] = msg.value;
    }

    modifier onlyOwner {
        require(owner == msg.sender);
        _;
    }

    function getPrice() public view returns(int){
         (,int price,,,) = priceFeed.latestRoundData();
        return price;
    }

    function withdraw() public onlyOwner payable {
        payable(msg.sender).transfer(address(this).balance);
    }
}