ney =float(input("enter your money: "))
numCoins =int(input("enter number of coins : "))
p = money/numCoins
wallet =dict()
# wallet ={(coin,round(p/amount,3)) for coin,amount in coins.items()}
num =0
for key,value in coins.items():
if num < numCoins:
wallet[key] = round(p/value,3)
num+=1
print(wallet)
