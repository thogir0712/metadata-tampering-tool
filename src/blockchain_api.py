from web3 import Web3
from datetime import datetime

def fetch_blockchain_data(tx_hash, infura_api_key):
    infura_url = f"https://mainnet.infura.io/v3/{infura_api_key}"
    w3 = Web3(Web3.HTTPProvider(infura_url))
    
    transaction = w3.eth.get_transaction(tx_hash)
    block = w3.eth.get_block(transaction['blockNumber'])
    
    #blockchain_stored_hash = "abc1234hashvalue"  
    
    return {
        "Transaction Hash": tx_hash,
        "Block Number": transaction['blockNumber'],
        "Timestamp": datetime.fromtimestamp(block['timestamp']),
        "From": transaction['from'],
        "To": transaction['to'],
        "Value (ETH)": w3.fromWei(transaction['value'], 'ether'),
        "File Hash (SHA256)": blockchain_stored_hash,
    }
