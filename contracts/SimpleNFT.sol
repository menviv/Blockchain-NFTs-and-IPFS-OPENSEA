//SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract SimpleNFT is ERC721 {

    uint256 public tokenCounter;

    constructor() public ERC721 ("Bird","BRD") {
        tokenCounter = 0;
    }

    function createNFT(string memory tokenURI) public returns (uint256) {
        uint newTokenId = tokenCounter;
        _safeMint(msg.sender,newTokenId);
        _setTokenURI(newTokenId, tokenURI);
        tokenCounter++;
        return newTokenId;
    }

}