import json
from algocid import Account, Asset, mainnet_algod_client, mainnet_indexer_client

account = Account(indexer_client=mainnet_indexer_client, algod_client=mainnet_algod_client)
asset = Asset(indexer_client=mainnet_indexer_client, algod_client=mainnet_algod_client)

address = "VYPDFMVRXCI2Z4FPC2GHB4QC6PSCTEDAS4EU7GE3W4B3MRHXNZO6BB2RZA"
asset_id = "312769"

print("##############################")
print("address:", address)
print("asset_id:", asset_id)
print("##############################")
# Account examples
# print(json.dumps(account.info(address), indent=4))
# print("balance:", account.balance(address, readable=True))
# print(account.balance(address))
# print("created asset ids", account.created_asset_ids(address))
# print("asset ids:", account.asset_ids(address))


# Asset examples
# print(json.dumps(asset.info(asset_id=asset_id), indent=4))
# print("asset creator:", asset.creator(asset_id=asset_id))
