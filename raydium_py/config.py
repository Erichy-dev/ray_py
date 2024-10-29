from solana.rpc.api import Client
from solders.keypair import Keypair #type: ignore
import base58

secret_key_list = [] # <secret_key>
secret_key_bytes = bytes(secret_key_list)

# Encode the bytes to base58
PRIV_KEY = base58.b58encode(secret_key_bytes).decode()
RPC = "" # https://api.mainnet-beta.solana.com
client = Client(RPC)
payer_keypair = Keypair.from_base58_string(PRIV_KEY)