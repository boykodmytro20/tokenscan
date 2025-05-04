# TokenScan - Web3 Token Tracker

TokenScan is a Web3 tool for analyzing token metrics, including token supply, holders, and smart contract source code. It leverages the **Etherscan API** to fetch data about Ethereum-based tokens.

📁 Project Structure

tokenscan/
 - app.py
 - templates/
   - index.html
 - static/
   - style.css
 - .env
 - requirements.txt
 - README.md
 - .gitignore

## 💡 Features

- Analyze token supply and volume
- View top holders (first 10)
- View the contract source code for any ERC-20 token

## 🛠 Tech Stack

- **Python** (Flask)
- **Etherscan API**
- **Web3.js** (for potential frontend integration)
- **Solidity** (for smart contracts, optional)

## 🏁 Getting Started

### 1. Clone the repository

```
git clone https://github.com/boykodmytro20/TokenScan.git
cd TokenScan
```

### 2. Create a virtual environment (optional but recommended)

```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Set your Etherscan API key

Create a .env file in the root of the project and add your Etherscan API key:

```
ETHERSCAN_API_KEY=your_etherscan_api_key_here
```

### 5. Run the app

```
python app.py
```

Visit http://127.0.0.1:5000 in your browser.

📫 Contact

Created by @boykodmytro20
