import json

from algocid import (Account, Asset, testnet_algod_client,
                     testnet_indexer_client)

account = Account(indexer_client=testnet_indexer_client, algod_client=testnet_algod_client)
asset = Asset(indexer_client=testnet_indexer_client, algod_client=testnet_algod_client)

address = "DUQR2JOFHCTNRRI546OZDYLCVBIVRYOSWKNR7A43YKVH437QS3XGJWTQ6I"
asset_id = "14704676"

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
