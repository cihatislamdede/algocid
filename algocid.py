import base64

import requests
from algosdk import v2client
from endpoints.indexer_endpoints import ALGONODE_INDEXER_MAINNET, ALGONODE_INDEXER_TESTNET

from endpoints.node_endpoints import ALGONODE_NODE_MAINNET, ALGONODE_NODE_TESTNET


def get_v2_algod_client(is_tesnet=False):
    if is_tesnet:
        return v2client.algod.AlgodClient(
            algod_address=ALGONODE_NODE_TESTNET, algod_token="", headers={"User-Agent": "algocid"}
        )
    else:
        return v2client.algod.AlgodClient(
            algod_address=ALGONODE_NODE_MAINNET, algod_token="", headers={"User-Agent": "algocid"}
        )


def get_v2_indexer_client(is_tesnet=False):
    if is_tesnet:
        return v2client.indexer.IndexerClient(indexer_address=ALGONODE_INDEXER_TESTNET, indexer_token="", headers={"User-Agent": "algocid"})
    else:
        return v2client.indexer.IndexerClient(indexer_address=ALGONODE_INDEXER_MAINNET, indexer_token="", headers={"User-Agent": "algocid"})


class Account:
    def __init__(self, algod_client: v2client.algod.AlgodClient, indexer_client: v2client.indexer.IndexerClient):
        self.algod_client = algod_client
        self.indexer_client = indexer_client

    def info(self, address: str):
        return self.indexer_client.account_info(address)

    def round(self):
        return self.indexer_client.health()["round"]

    def balance(self, address: str, readable: bool = False):
        balance = self.indexer_client.account_info(address)["account"]["amount"]
        if readable:
            return balance / 10**6
        return balance

    def created_asset_ids(self, account_address: str):
        account_info = self.algod_client.account_info(account_address)
        created_asset_ids = [asset["index"] for asset in account_info["created-assets"]]
        return created_asset_ids

    def asset_ids(self, account_address: str):
        account_info = self.algod_client.account_info(account_address)
        asset_ids = [asset["asset-id"] for asset in account_info["assets"]]
        return asset_ids

    def is_holder(self, account_address: str, creator_addresses: list):
        creator_assets = []
        for creator_address in creator_addresses:
            creator_assets += self.created_asset_ids(creator_address)
        account_info = self.algod_client.account_info(account_address)
        account_assets = [asset["asset-id"] for asset in account_info["assets"] if asset["amount"] > 0]
        return any(asset_id in creator_assets for asset_id in account_assets)


class Asset:
    def __init__(self, algod_client: v2client.algod.AlgodClient, indexer_client: v2client.indexer.IndexerClient):
        self.algod_client = algod_client
        self.indexer_client = indexer_client

    def info(self, asset_id: str):
        return self.indexer_client.asset_info(asset_id)

    def round(self):
        return self.indexer_client.health()["round"]

    def params(self, asset_id: str):
        return self.indexer_client.asset_info(asset_id)["asset"]["params"]

    def name(self, asset_id: str):
        return self.params(asset_id)["name"]

    def unit_name(self, asset_id: str):
        return self.params(asset_id)["unit-name"]

    def url(self, asset_id: str):
        return self.params(asset_id)["url"]

    def creator(self, asset_id: str):
        return self.params(asset_id)["creator"]

    def metadata(self, asset_id: str):
        req = requests.get(f"https://mainnet-idx.algonode.cloud/v2/assets/{asset_id}/transactions?tx-type=acfg").json()["transactions"]
        note = req[len(req) - 1]["note"]
        return base64.b64decode(note).decode("utf-8")

    def holders(self, asset_id: str, only_wallets: bool = False):
        if not only_wallets:
            return requests.get(f"https://mainnet-idx.algonode.cloud/v2/assets/{asset_id}/balances?currency-greater-than=0").json()["balances"]
        else:
            holders = requests.get(f"https://mainnet-idx.algonode.cloud/v2/assets/{asset_id}/balances?currency-greater-than=0").json()["balances"]
            return [holder["address"] for holder in holders]
