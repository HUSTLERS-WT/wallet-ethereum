from eth_keys import keys
from eth_account import Account
import os

# Generate a 32-byte (256-bit) random private key
private_key_bytes = os.urandom(32)
private_key = keys.PrivateKey(private_key_bytes)

# Generate the public key
public_key = private_key.public_key

# Generate the Ethereum address
eth_address = public_key.to_checksum_address()

with open("walletDetails.dat", "w") as f:
    f.write(f"Private Key: {private_key.to_hex()}\n")
    f.write(f"Public Key: {public_key}\n")
    f.write(f"Ethereum Address: {eth_address}\n")

with open("privatekey.dat", "w") as f:
    f.write(f"{private_key.to_hex()}")

print("Wallet details saved to walletDetails.dat and private key saved to privatekey.dat")
