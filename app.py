import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")

def get_token_info(contract_address):
    base_url = "https://api.etherscan.io/api"

    # Token supply
    supply_res = requests.get(base_url, params={
        "module": "stats",
        "action": "tokensupply",
        "contractaddress": contract_address,
        "apikey": ETHERSCAN_API_KEY
    })

    # Token holders
    holders_res = requests.get(base_url, params={
        "module": "token",
        "action": "tokenholderlist",
        "contractaddress": contract_address,
        "page": 1,
        "offset": 10,
        "apikey": ETHERSCAN_API_KEY
    })

    # Token contract source
    source_res = requests.get(base_url, params={
        "module": "contract",
        "action": "getsourcecode",
        "address": contract_address,
        "apikey": ETHERSCAN_API_KEY
    })

    return {
        "supply": supply_res.json(),
        "holders": holders_res.json(),
        "source": source_res.json()
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    token_data = None
    if request.method == 'POST':
        contract_address = request.form['contract']
        token_data = get_token_info(contract_address)
    return render_template("index.html", token_data=token_data)

if __name__ == '__main__':
    app.run(debug=True)
