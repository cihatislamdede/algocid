import json
from algocid import Account, Asset, mainnet_algod_client, mainnet_indexer_client

account = Account(indexer_client=mainnet_indexer_client, algod_client=mainnet_algod_client)
asset = Asset(indexer_client=mainnet_indexer_client, algod_client=mainnet_algod_client)

address = "7BZEUIEPHZGDK6E673DVOY6BVCCZC6YFAJ3QWROPBZK5XKGE5GUWDYZRUY"
asset_id = "312769"

# Account examples
print(json.dumps(account.info(address), indent=4))
print(account.balance(address, readable=True))
print(account.balance(address))


# Asset examples
print(json.dumps(asset.info(asset_id=asset_id), indent=4))
print(asset.creator(asset_id=asset_id))
