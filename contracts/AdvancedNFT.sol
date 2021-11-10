//AdvancedNFT
//SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@openzeppelin/contracts/access/Ownable.sol";


contract AdvancedNFT is ERC721, VRFConsumerBase {
    uint256 public tokenCounter;
    bytes32 public keyHash;
    uint256 public fee;

    enum Breed{K1, K2, K3}

    mapping(uint256=>Breed) public tokenIdBreed;

    mapping(bytes32=>address) public requestIdToSender;

    event requestedNFT(bytes32 indexed requestId, address requester);

    event breedAssigned(uint256 indexed tokenId, Breed selectedBreed);


    constructor(address _vrfCoordinator, address _linkToken, bytes32 _keyHash, uint256 _fee) public
    VRFConsumerBase(_vrfCoordinator, _linkToken)
    ERC721("Bird","BRD")
    {
        tokenCounter=0;
        keyHash = _keyHash;
        fee = _fee;

    }

    function createAdvanceNft() public returns (bytes32) {
        bytes32  requestId = requestRandomness(keyHash, fee);
        requestIdToSender[requestId] = msg.sender;
        emit requestedNFT(requestId, msg.sender);
    }

    /// internal = only the VRFCoordinator can call this function
    /// Overide the inherited function
    function fulfillRandomness(bytes32 requestId, uint256 randomNumber) internal override {
        Breed selectedBreed = Breed(randomNumber%3);
        uint256 newTokenId = tokenCounter;

        tokenIdBreed[newTokenId] = selectedBreed;
        emit breedAssigned(newTokenId, selectedBreed);

        address owner = requestIdToSender[requestId];
        _safeMint(owner,newTokenId);
        
        //_setTokenURI(newTokenId, tokenURI);
        tokenCounter++;
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        /// K1 K2 K3
        require(_isApprovedOrOwner(_msgSender(), tokenId), "ERC721: Caller is not owner or approved");
        _setTokenURI(tokenId, _tokenURI);
    }



}