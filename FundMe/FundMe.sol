// SPDX-License-Identifier: MIT
// Kovan-netowrk

pragma solidity >= 0.6.0 <0.9.0;

//interfaces - functions to implement, compile down to ABI
//ABI applicaiton-binary-interfsace - tells solidity what functions can be called on another contract. you need this if you wanna call another contract
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

//We want this contract to be payable
//Whenever you make a transaction you can append a value 
//msg.sender - represents the sender of the function call
//msg.value - the value they sent
//chainlink - decentralized data ie. crypto maket prices 

contract FundMe {

mapping(address => uint256) public addressToAmountFunded;

//A function that will keep track of how much money is being sent 
function fund() public payable {
    addressToAmountFunded[msg.sender] += msg.value;
    //conversion rathers instead of eth -- find the eth -> usd conversion value   
} 

//Reading from another contract 
function getVersion() public view returns (uint256) {  
    //We have this contract that has the interface functions implemented, we just pass the address of a data feed in order. ETH-USD
    AggregatorV3Interface priceFeed = AggregatorV3Interface(0x9326BFA02ADD2366b30bacB125260Af641031331); 
    return priceFeed.version();
}

}