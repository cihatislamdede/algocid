from algocid import Account, Asset, mainnet_algod_client, mainnet_indexer_client

account = Account(indexer_client=mainnet_indexer_client, algod_client=mainnet_algod_client)
asset = Asset(indexer_client=mainnet_indexer_client, algod_client=mainnet_algod_client)

print(account.get_balance("7BZEUIEPHZGDK6E673DVOY6BVCCZC6YFAJ3QWROPBZK5XKGE5GUWDYZRUY", readable=True))
print(account.get_balance("7BZEUIEPHZGDK6E673DVOY6BVCCZC6YFAJ3QWROPBZK5XKGE5GUWDYZRUY"))
print(asset.get_creator(asset_id=312769))
