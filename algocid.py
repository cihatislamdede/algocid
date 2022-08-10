import base64
from ast import literal_eval

import requests
from algosdk import v2client

from constants import (ALGONODE_INDEXER_MAINNET, ALGONODE_INDEXER_TESTNET,
                       ALGONODE_NODE_MAINNET, ALGONODE_NODE_TESTNET,
                       IS_TESTNET)


def get_v2_algod_client(is_tesnet=IS_TESTNET):
    if is_tesnet:
        return v2client.algod.AlgodClient(
            algod_address=ALGONODE_NODE_TESTNET, algod_token="", headers={"User-Agent": "algocid"}
        )
    else:
        return v2client.algod.AlgodClient(
            algod_address=ALGONODE_NODE_MAINNET, algod_token="", headers={"User-Agent": "algocid"}
        )


def get_v2_indexer_client(is_tesnet=IS_TESTNET):
    if is_tesnet:
        return v2client.indexer.IndexerClient(indexer_address=ALGONODE_INDEXER_TESTNET, indexer_token="", headers={"User-Agent": "algocid"})
    else:
        return v2client.indexer.IndexerClient(indexer_address=ALGONODE_INDEXER_MAINNET, indexer_token="", headers={"User-Agent": "algocid"})


indexer_request_url = f"{ALGONODE_INDEXER_TESTNET}/v2" if IS_TESTNET else f"{ALGONODE_INDEXER_MAINNET}/v2"
node_request_url = f"{ALGONODE_NODE_TESTNET}/v2" if IS_TESTNET else f"{ALGONODE_NODE_MAINNET}/v2"


class AccountFetcher:
    def __init__(self, algod_client: v2client.algod.AlgodClient, indexer_client: v2client.indexer.IndexerClient):
        self.algod_client = algod_client
        self.indexer_client = indexer_client

    def info(self, address: str) -> dict:
        '''
        Returns the account info.
        '''
        return self.indexer_client.account_info(address)

    def round(self) -> int:
        '''
        Returns the current round.
        '''
        return self.indexer_client.health()["round"]

    def balance(self, address: str, readable: bool = False) -> float or int:
        '''
        Returns the balance of the account.\n
        readable: If True, returns the balance in readable format. (default: False, returns the balance in microAlgos format.)
        '''
        balance = self.indexer_client.account_info(address)["account"]["amount"]
        if readable:
            return balance / 10**6
        return balance

    def created_asset_ids(self, account_address: str) -> list:
        '''
        Returns the asset ids of the assets created by the account.
        '''
        account_info = self.algod_client.account_info(account_address)
        created_asset_ids = [asset["index"] for asset in account_info["created-assets"]]
        return created_asset_ids

    def asset_ids(self, account_address: str) -> list:
        '''
        Returns the asset ids of the assets the account has.
        '''
        account_info = self.algod_client.account_info(account_address)
        asset_ids = [asset["asset-id"] for asset in account_info["assets"]]
        return asset_ids

    def is_holder(self, account_address: str, creator_addresses: list) -> bool:
        '''
        Check if the account is a holder of any of the assets created by the creator addresses.
        '''
        creator_assets = []
        for creator_address in creator_addresses:
            creator_assets += self.created_asset_ids(creator_address)
        account_info = self.algod_client.account_info(account_address)
        account_assets = [asset["asset-id"] for asset in account_info["assets"] if asset["amount"] > 0]
        return any(asset_id in creator_assets for asset_id in account_assets)


class AssetFetcher:
    def __init__(self, algod_client: v2client.algod.AlgodClient, indexer_client: v2client.indexer.IndexerClient):
        self.algod_client = algod_client
        self.indexer_client = indexer_client

    def info(self, asset_id: str) -> dict:
        '''
        Returns the asset info.
        '''
        return self.indexer_client.asset_info(asset_id)

    def round(self) -> int:
        '''
        Returns the current round.
        '''
        return self.indexer_client.health()["round"]

    def params(self, asset_id: str) -> dict:
        '''
        Returns the asset params.
        '''
        return self.indexer_client.asset_info(asset_id)["asset"]["params"]

    def name(self, asset_id: str) -> str:
        '''
        Returns the asset name.
        '''
        return self.params(asset_id)["name"]

    def unit_name(self, asset_id: str) -> str:
        '''
        Returns the asset unit-name.
        '''
        return self.params(asset_id)["unit-name"]

    def url(self, asset_id: str) -> str:
        '''
        Returns the asset url.
        '''
        try:
            return self.metadata(asset_id)["url"]
        except KeyError:
            print("No url found for asset!")
            return ""

    def creator(self, asset_id: str) -> str:
        '''
        Returns the asset creator.
        '''
        return self.params(asset_id)["creator"]

    def metadata(self, asset_id: str) -> dict:
        '''
        Returns the asset metadata.
        '''
        try:
            req = requests.get(f"{indexer_request_url}/assets/{asset_id}/transactions?tx-type=acfg").json()["transactions"]
            note = req[len(req) - 1]["note"]
            return literal_eval(base64.b64decode(note).decode("utf-8"))
        except KeyError:
            print("No metadata found for asset!")
            return {}
        except Exception as e:
            print(e)
            return {}

    def holders(self, asset_id: str, only_wallets: bool = False) -> list:
        '''
        Returns the asset holders.\n
        only_wallets: If True, only returns the wallets that hold the asset. (default: False)
        '''
        if not only_wallets:
            return requests.get(f"{indexer_request_url}/assets/{asset_id}/balances?currency-greater-than=0").json()["balances"]
        else:
            holders = requests.get(f"{indexer_request_url}/assets/{asset_id}/balances?currency-greater-than=0").json()["balances"]
            return [holder["address"] for holder in holders]


class TransactionFetcher:
    def __init__(self, algod_client: v2client.algod.AlgodClient, indexer_client: v2client.indexer.IndexerClient):
        self.algod_client = algod_client
        self.indexer_client = indexer_client

    def info(self, transaction_id: str) -> dict:
        '''
        Returns the transaction info.
        '''
        return self.indexer_client.transaction(transaction_id)["transaction"]
