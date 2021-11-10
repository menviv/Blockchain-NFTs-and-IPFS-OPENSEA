from scripts.helpful_scripts import get_account
from brownie import SimpleNFT

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


def deploy():
    account=get_account()
    simpleNft = SimpleNFT.deploy({"from": account})
    tx = simpleNft.createNFT(sample_token_uri, {"from": account})
    tx.wait(1)
    print(
        f"You can view your NFT at : {OPENSEA_URL.format(simpleNft.address, simpleNft.tokenCounter()-1)}"
    )
    return simpleNft

def main():
    deploy()