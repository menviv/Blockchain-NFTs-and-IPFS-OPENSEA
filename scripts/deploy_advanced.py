from scripts.helpful_scripts import get_account, OPENSEA_URL, LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_contract, fund_with_linktoken
from brownie import AdvancedNFT, config, network




def deploy():
    account=get_account()
    advancedNFT = AdvancedNFT.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["key_hash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"]
        )
    fund_with_linktoken(advancedNFT.address, account)
    tx = advancedNFT.createAdvanceNft({"from": account})
    tx.wait(1)
    print("You NFT was created successfully")
    return advancedNFT



def main():
    deploy()