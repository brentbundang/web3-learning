// SPDX-License-Identifier: MIT
// Rinkeby-netowrk

pragma solidity >=0.6.6 <0.9.0;

//interfaces - functions to implement, compile down to ABI
//ABI applicaiton-binary-interfsace - tells solidity what functions can be called on another contract. you need this if you wanna call another contract
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
//import "@chainlink/contracts/src/v0.8/vendor/SafeMathChainlink.sol"; //doesn't allow for overflows, don't have to account for overflows starting Soliditiy 0.8

//We want this contract to be payable
//Whenever you make a transaction you can append a value 
//msg.sender - represents the sender of the function call
//msg.value - the value they sent
//chainlink - decentralized data ie. crypto maket prices 

contract FundMe {

    mapping(address => uint256) public addressToAmountFunded;
    address public owner; 

    constructor(){
        owner = msg.sender;
    }

    //A function that will keep track of how much money is being sent 
    // See if the value they sent us is greater too or less than 50 dollars 
    function fund() public payable {
        // 50
        uint256 minimumUSD = 50 * 10 ** 18; //Represented in gwei
        require(getConversionRate(msg.value) >= minimumUSD, "You need to spend more ETH!"); //stop executing if not true, revert the transaction -- receommended
        
        addressToAmountFunded[msg.sender] += msg.value;
        //conversion rathers instead of eth -- find the eth -> usd conversion value   
    } 

    //Reading from another contract 
    function getVersion() public view returns (uint256) {  
        //We have this contract that has the interface functions implemented, we just pass the address of a data feed in order. ETH-USD
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e); 
        return priceFeed.version();
    }

    //Returns 5 values
    //Tuple is a list of objects of potentially different types whos number is a constant at compile time 
    function getPrice() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e); 
        /*((uint80 roundId,
        int256 answer,
        uint256 startedAt, 
        uint256 updatedAt,
        uint80 answeredInRound) = priceFeed.latestRoundData();*/
        (,int256 answer,,,) = priceFeed.latestRoundData(); //Use commas to remove the warnings about unused local variables
        // ETH/USD rate in 18 digit 
         return uint256(answer * 10000000000);
    }

    //1000000000
    function getConversionRate(uint256 ethAmount) public view returns (uint256){
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1000000000000000000;
        // the actual ETH/USD conversation rate, after adjusting the extra 0s.
        return ethAmountInUsd;
    }

    function withdraw() public payable {
        require(msg.sender == owner); //If the sender is the owner transfer the balence they have sent to this contract based on this contracts address
        payable(msg.sender).transfer(address(this).balance); //Have set the address as payable
    }

}