#!/usr/bin/python3

import sys
#sys.path.append("/home/ubuntu/workspace/cosmospy")

from fridaypy import generate_wallet

wallet = generate_wallet()
#print(wallet)
dataList=[]
dataList.append(":".join(["\"private_key\"","\"" + wallet["private_key"] + "\""]))
dataList.append(":".join(["\"public_key\"","\"" + wallet["public_key"] + "\""]))
dataList.append(":".join(["\"address\"","\"" + wallet["address"] + "\""]))
dataList.append(":".join(["\"mnemonic\"","\"" + wallet["mnemonic"] + "\""]))
data = "{" + ",".join(dataList) + "}"
print(data)
