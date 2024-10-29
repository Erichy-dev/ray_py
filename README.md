# raydium_py

This repo is for my python lovers who want to trade on Raydium. Only works for SOL pairs. 

Clone the repo, add Private Key (base58 string) and RPC url to the config.py.

**If you can - please support my work and donate to: 3pPK76GL5ChVFBHND54UfBMtg36Bsh1mzbQPTbcK89PD**

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

**What format should my private key be in?** 

The private key should be in the base58 string format, not bytes. 

**Why are my transactions being dropped?** 

You get what you pay for. Don't use the main-net RPC, just spend the money for Helius or Quick Node.

**How do I change the fee?** 

Modify the UNIT_BUDGET and UNIT_PRICE in the constants.py. 

### Contact

My services are for **hire**. Contact me if you need help integrating the code into your own project. 

Telegram: @AL_THE_BOT_FATHER
