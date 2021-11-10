from brownie import AdvancedNFT, config, network
from scripts.helpful_scripts import get_account, OPENSEA_URL, LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_contract, fund_with_linktoken
from web3 import Web3


def main():
    print(AdvancedNFT[-1])
    account = get_account()
    advanced_collect = AdvancedNFT[-1]
    fund_with_linktoken(advanced_collect.address, amount = Web3.toWei(1, "ether"))
    creartion_transaction = advanced_collect.createAdvanceNft({"from": account})
    creartion_transaction.wait(1)
    print("creartion of collection succeeded")
