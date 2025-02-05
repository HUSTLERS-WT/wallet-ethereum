from web3 import Web3
from eth_account import Account

# Connect to Sepolia Testnet
web3 = Web3(Web3.HTTPProvider("https://ethereum-sepolia.publicnode.com"))

# Sender's Private Key (NEVER expose in production)
private_key = "0x2034bba41b7dfc91b12d25d3a60b10b40ac139534202d643228e06802c0ab17c"

# Derive Sender's Address
account = Account.from_key(private_key)
sender_address = account.address

# Print balance before sending transaction
balance = web3.from_wei(web3.eth.get_balance(sender_address), "ether")
print(f"Sender Balance: {balance} ETH")

if balance < 0.002:  # Ensure enough balance for transaction + gas
    raise Exception("Insufficient balance! Get Sepolia ETH from a faucet.")

# Define Recipient Address & Amount
recipient_address = "0x08335edd20C6c03754607664224B67e534FDf228"
amount_eth = 0.001  # Amount to send in ETH
amount_wei = web3.to_wei(amount_eth, "ether")

# Get Nonce
nonce = web3.eth.get_transaction_count(sender_address)

# Lower Gas Price to Reduce Cost
gas_price = web3.to_wei(25, "gwei")  # Manually set a lower gas price
gas_limit = 21000  # Standard gas limit for ETH transfers

# Construct Transaction
transaction = {
    'nonce': nonce,
    'to': recipient_address,
    'value': amount_wei,
    'gas': gas_limit,
    'gasPrice': gas_price,
    'chainId': 11155111  # Sepolia Testnet Chain ID
}

# Sign Transaction
signed_tx = web3.eth.account.sign_transaction(transaction, private_key)

# Broadcast Transaction
tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)

# Print Transaction Hash
print("Transaction Sent!")
print("Transaction Hash:", web3.to_hex(tx_hash))
