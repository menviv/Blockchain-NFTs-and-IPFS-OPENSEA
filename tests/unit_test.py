from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    FORKED_LOCAL_ENVIRONMENTS,
    get_account,
)
from scripts.deploy import deploy
from brownie import network
import pytest

def test_can_create_simple_nft():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    simple_nft = deploy()
    assert simple_nft.ownerOf(0) == get_account()