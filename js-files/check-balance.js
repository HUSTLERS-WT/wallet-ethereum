const { Web3, HttpProvider } = require("web3"); // Import both Web3 and HttpProvider

// Connect to an Ethereum node
const web3 = new Web3(new HttpProvider("https://ethereum-sepolia.publicnode.com"));

// Replace with your Ethereum wallet address
const walletAddress = "0x53F866A0B939BdAa2DB49815CE5F3D006Fd068De";

async function getBalance() {0x53F866A0B939BdAa2DB49815CE5F3D006Fd068De
    try {
        // Get balance in Wei
        const balanceWei = await web3.eth.getBalance(walletAddress);

        // Convert Wei to Ether
        const balanceEth = web3.utils.fromWei(balanceWei, "ether");

        console.log(`Wallet Balance: ${balanceEth} ETH`);
    } catch (error) {
        console.error("Error fetching balance:", error);
    }
}

// Call the function
getBalance();
