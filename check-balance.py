from web3 import Web3

# Connect to an Ethereum node (Infura, Alchemy, or local node)
# web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"))
# web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/884aa99cbb624e03ae13bc1d8091e3a5"))
# web3 = Web3(Web3.HTTPProvider("https://rpc.holesky.ethpandaops.io"))
web3 = Web3(Web3.HTTPProvider("https://ethereum-sepolia.publicnode.com"))

# Replace with your Ethereum wallet address
wallet_address = "0xe1d0526DcEb3F5Ed1518580470f477276D1adeEC"
# wallet_address = "0x53F866A0B939BdAa2DB49815CE5F3D006Fd068De"

# Get balance in Wei (1 ETH = 10**18 Wei)
balance_wei = web3.eth.get_balance(wallet_address)

# Convert to Ether
balance_eth = web3.from_wei(balance_wei, "ether")

print(f"Wallet Balance: {balance_eth} ETH")
