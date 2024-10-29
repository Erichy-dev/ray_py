# raydium_py

This repo is for my python lovers who want to trade on Raydium. Only works for SOL pairs. 

Clone the repo, add Private Key (base58 string) and RPC url to the config.py.

### Examples

```
from raydium import buy
from utils import get_pair_address

# Buy Example
token_address = "7GCihgDB8fe6KNjn2MYtkzZcRjQy3t9GHdC8uHYmW2hr" # POPCAT
pair_address = get_pair_address(token_address)
sol_in = .1
slippage = 5
buy(pair_address, sol_in, slippage)
```

```
from raydium import sell
from utils import get_pair_address

# Sell Example
token_address = "7GCihgDB8fe6KNjn2MYtkzZcRjQy3t9GHdC8uHYmW2hr" # POPCAT
pair_address = get_pair_address(token_address)
percentage = 100
slippage = 5
sell(pair_address, percentage, slippage)
```


### FAQS

**Why are my transactions being dropped?** 

You get what you pay for. Don't use the main-net RPC, just spend the money for Helius or Quick Node.

**How do I change the fee?** 

Modify the UNIT_BUDGET and UNIT_PRICE in the constants.py. 
