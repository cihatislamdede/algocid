from algosdk import v2client

from endpoints.indexer_endpoints import (ALGONODE_INDEXER_MAINNET,
                                         ALGONODE_INDEXER_TESTNET)
from endpoints.node_endpoints import (ALGONODE_NODE_MAINNET,
                                      ALGONODE_NODE_TESTNET)

testnet_algod_client = algod_client = v2client.algod.AlgodClient(algod_address=ALGONODE_NODE_TESTNET, algod_token="", headers={"User-Agent": "algosdk"})
mainnet_algod_client = algod_client = v2client.algod.AlgodClient(algod_address=ALGONODE_NODE_MAINNET, algod_token="", headers={"User-Agent": "algosdk"})

testnet_indexer_client = v2client.indexer.IndexerClient(indexer_address=ALGONODE_INDEXER_TESTNET, indexer_token="", headers={"User-Agent": "algosdk"})
mainnet_indexer_client = v2client.indexer.IndexerClient(indexer_address=ALGONODE_INDEXER_MAINNET, indexer_token="", headers={"User-Agent": "algosdk"})


class Account:
    def __init__(self, algod_client: v2client.algod.AlgodClient, indexer_client: v2client.indexer.IndexerClient):
        self.algod_client = algod_client
        self.indexer_client = indexer_client

    def get_balance(self, address: str, readable: bool = False):
        balance = self.indexer_client.account_info(address)["account"]["amount"]
        if readable:
            return "{:,}".format(balance / 10**6)
        return balance


class Asset:
    def __init__(self, algod_client: v2client.algod.AlgodClient, indexer_client: v2client.indexer.IndexerClient):
        self.algod_client = algod_client
        self.indexer_client = indexer_client

    def get_creator(self, asset_id: str):
        return self.indexer_client.asset_info(asset_id)["asset"]["params"]["creator"]
