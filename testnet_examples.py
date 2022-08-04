from algocid import AccountFetcher, AssetFetcher, get_v2_algod_client, get_v2_indexer_client

account = AccountFetcher(indexer_client=get_v2_indexer_client(is_tesnet=True), algod_client=get_v2_algod_client(is_tesnet=True))
asset = AssetFetcher(indexer_client=get_v2_indexer_client(is_tesnet=True), algod_client=get_v2_algod_client(is_tesnet=True))

address = "VETIGP3I6RCUVLVYNDW5UA2OJMXB5WP6L6HJ3RWO2R37GP4AVETICXC55I"
asset_id = "10458941"

print("##############################")
print("address:", address)
print("asset_id:", asset_id)
print("##############################")
# Account examples
# print(account.info(address))
# print("balance:", account.balance(address, readable=True))
# print(account.balance(address))
# print("created asset ids", account.created_asset_ids(address))
# print("asset ids:", account.asset_ids(address))


# Asset examples
# print(asset.info(asset_id=asset_id))
# print("asset creator:", asset.creator(asset_id=asset_id))
# print(asset.creator(asset_id))
# print(asset.name(asset_id))
# print(asset.unit_name(asset_id))
# print(asset.url(asset_id))
# print(asset.params(asset_id))
# print(asset.holders(asset_id))
# print(asset.holders(asset_id, only_wallets=True))
