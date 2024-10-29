from solana.rpc.api import Client
from solders.keypair import Keypair #type: ignore
import base58

secret_key_list = [96,51,82,208,233,96,86,196,211,176,121,177,143,219,70,220,127,80,1,154,77,27,238,236,225,235,242,215,245,64,98,199,127,255,67,90,37,127,59,102,91,178,244,201,88,80,209,201,219,240,242,234,29,49,111,49,250,92,22,66,166,23,216,169]
secret_key_bytes = bytes(secret_key_list)

# Encode the bytes to base58
PRIV_KEY = base58.b58encode(secret_key_bytes).decode()
RPC = "https://api.mainnet-beta.solana.com"
client = Client(RPC)
payer_keypair = Keypair.from_base58_string(PRIV_KEY)