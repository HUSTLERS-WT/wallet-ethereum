from web3 import Web3

# Connect to an Ethereum node (Infura, Alchemy, or local node)
# web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"))
# web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/884aa99cbb624e03ae13bc1d8091e3a5"))
web3 = Web3(Web3.HTTPProvider("https://rpc.holesky.ethpandaops.io"))

# Replace with your Ethereum wallet address
wallet_address = "0x1665a01616299e6b7e993f8eAE4cd75AD6E184ae"

# Get balance in Wei (1 ETH = 10**18 Wei)
balance_wei = web3.eth.get_balance(wallet_address)

# Convert to Ether
balance_eth = web3.from_wei(balance_wei, "ether")

print(f"Wallet Balance: {balance_eth} ETH")
