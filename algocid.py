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

    def info(self, address: str):
        return self.indexer_client.account_info(address)

    def balance(self, address: str, readable: bool = False):
        balance = self.indexer_client.account_info(address)["account"]["amount"]
        if readable:
            return "{:,}".format(balance / 10**6)
        return balance

    def created_asset_ids(self, account_address):
        account_info = self.algod_client.account_info(account_address)
        created_asset_ids = [asset["index"] for asset in account_info["created-assets"]]
        return created_asset_ids

    def asset_ids(self, account_address):
        account_info = self.algod_client.account_info(account_address)
        asset_ids = [asset["asset-id"] for asset in account_info["assets"]]
        return asset_ids


class Asset:
    def __init__(self, algod_client: v2client.algod.AlgodClient, indexer_client: v2client.indexer.IndexerClient):
        self.algod_client = algod_client
        self.indexer_client = indexer_client

    def info(self, asset_id: str):
        return self.indexer_client.asset_info(asset_id)

    def creator(self, asset_id: str):
        return self.indexer_client.asset_info(asset_id)["asset"]["params"]["creator"]
