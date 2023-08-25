import requests
import base64


def get_transaction_data(block_num):
    #base_url = "https://api.mintscan.io/akash/v1"
    base_url = "https://www.mintscan.io/akash/blocks/"
    url = f"{base_url}{block_num}"

    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json().get("data", {})
            txs_base64 = data.get("txs", "")

            if txs_base64:
                txs_decoded = base64.b64decode(txs_base64).decode("utf-8")
                return txs_decoded
            else:
                return "No transactions in this block."
        except requests.exceptions.JSONDecodeError:
            return "Invalid JSON data in the response."
    else:
        return f"Error. Status code: {response.status_code}"

block_number = 11260637
transaction_data = get_transaction_data(block_number)
print(transaction_data)
