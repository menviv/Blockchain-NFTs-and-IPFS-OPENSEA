
from brownie import network, AdvancedNFT
from scripts.helpful_scripts import get_account, getBreed, get_account, OPENSEA_URL

k_meta_dic = {
    "k1": "https://ipfs.io/ipfs/QmbFMke1KXqnYyBBWxB74N4c5SBnJMVAiMNRcGu6x1AwQH?filename=0-k1.json",
    "k2": "https://ipfs.io/ipfs/QmbFMke1KXqnYyBBWxB74N4c5SBnJMVAiMNRcGu6x1AwQH?filename=2-k2.json",
    "k3": "https://ipfs.io/ipfs/QmbFMke1KXqnYyBBWxB74N4c5SBnJMVAiMNRcGu6x1AwQH?filename=1-k3.json"
}

def main():
    print(f"working on {network.show_active()}")
    collection = AdvancedNFT[-1]
    number_of_nfts = collection.tokenCounter()
    print(f"You have created {number_of_nfts} nfts")
    for tokenid in range(number_of_nfts):
        print(f"tokenid: {tokenid}")
        breed = getBreed(collection.tokenIdBreed(tokenid))
        if not collection.tokenURI(tokenid).startswith("https"):
            print(f"Setting tokenURI of {tokenid}")
            set_tokenURI(tokenid, collection.address, k_meta_dic[breed])


def set_tokenURI(tokenid, nft_contract, tokenURI):
    account=get_account()
    tx =nft_contract.setTokenURI(tokenid, tokenURI, {"from": account})
    tx.wait(1)
    print(f"Great! you can view your NFT at: {OPENSEA_URL.format(nft_contract.address, tokenid)}")
    print("Please wait up to 20 minutes..")
