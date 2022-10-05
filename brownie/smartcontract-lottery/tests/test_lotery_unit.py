from brownie import Lottery, accounts, config, network
from scripts.deploy_lottery import deploy_lottery
from web3 import Web3


def test_get_entrance_fee():
    lottery = deploy_lottery()

    expected_entrance_fee = Web3.toWei(0.025, "ether")

    entrance_fee = lottery.getEntranceFee()
    print(f"EXPedted: {expected_entrance_fee}")
    print(f"Entrance: {entrance_fee}")

    assert expected_entrance_fee == entrance_fee
