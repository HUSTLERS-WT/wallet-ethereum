from web3 import Web3

rpc_url = "https://ethereum-holesky.publicnode.com"  # Use a public RPC URL
w3 = Web3(Web3.HTTPProvider(rpc_url))

raw_tx = "0x416b2856eaaebae6e0fff36b7d9593fc97714633d3b4466a350d132a9f182251047f54c81f8203502843000000010698d0100000818d010"

try:
    tx_hash = w3.eth.send_raw_transaction(bytes.fromhex(raw_tx[2:]))  # Remove "0x" prefix
    print("Transaction Hash:", tx_hash.hex())
except Exception as e:
    print("Error:", e)

