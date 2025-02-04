const { ethers } = require("ethers");
const fs = require("fs");

// Generate a random wallet
const wallet = ethers.Wallet.createRandom();

const privateKey = wallet.privateKey;
const publicKey = wallet.publicKey;
const ethAddress = wallet.address;

// Save wallet details to a file
fs.writeFileSync("walletDetails.dat", `Private Key: ${privateKey}\nPublic Key: ${publicKey}\nEthereum Address: ${ethAddress}\n`);
fs.writeFileSync("privatekey.dat", privateKey);

console.log("Wallet details saved to walletDetails.dat and private key saved to privatekey.dat");
