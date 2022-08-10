from algocid import (AccountFetcher, AssetFetcher, TransactionFetcher,
                     get_v2_algod_client, get_v2_indexer_client)
from constants import IS_TESTNET

account_fetcher = AccountFetcher(indexer_client=get_v2_indexer_client(is_tesnet=IS_TESTNET), algod_client=get_v2_algod_client(is_tesnet=IS_TESTNET))
asset_fetcher = AssetFetcher(indexer_client=get_v2_indexer_client(is_tesnet=IS_TESTNET), algod_client=get_v2_algod_client(is_tesnet=IS_TESTNET))
transaction_fetcher = TransactionFetcher(indexer_client=get_v2_indexer_client(is_tesnet=IS_TESTNET), algod_client=get_v2_algod_client(is_tesnet=IS_TESTNET))

if IS_TESTNET:
    address = "VETIGP3I6RCUVLVYNDW5UA2OJMXB5WP6L6HJ3RWO2R37GP4AVETICXC55I"
    asset_id = "10458941"
    transaction_id = "PU6ZNPD563QETUFMGLFCWN4OKBZQKXGY3E64DYEWUY23KKZ5TJ7A"
else:
    address = "D5J7H7PIYKLY2U6A5OFUAC7GQHTHSXXNX65DSD3CJYPBV2MVK6NTNW44CA"
    asset_id = "326189642"
    transaction_id = "VNYJRN44VLJ5VSFLJRQQNC4PG5FDQOL2BYAWIIKVZIEEJFUJLKZA"

print("##############################")
print("address:", address)
print("asset_id:", asset_id)
print("##############################")
# AccountFetcher examples
# print(account_fetcher.info(address))
# print("balance:", account_fetcher.balance(address, readable=True))
# print(account_fetcher.balance(address))
# print("created asset_fetcher ids", account_fetcher.created_asset_ids(address))
# print("asset_fetcher ids:", account_fetcher.asset_ids(address))


# AssetFetcher examples
# print(asset_fetcher.info(asset_id=asset_id))
# print("asset_fetcher creator:", asset_fetcher.creator(asset_id=asset_id))
# print(asset_fetcher.creator(asset_id))
# print(asset_fetcher.name(asset_id))
# print(asset_fetcher.unit_name(asset_id))
# print(asset_fetcher.url(asset_id))
# print(asset_fetcher.params(asset_id))
# print(asset_fetcher.metadata(326189642))
# print(asset_fetcher.holders(asset_id))
# print(asset_fetcher.holders(asset_id, only_wallets=True))


# TransactionFetcher examples
# print(transaction_fetcher.info(transaction_id=transaction_id))
