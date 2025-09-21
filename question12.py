# Question No 12
# Currency Converter (USD to PKR)
# Input amount in USD. Convert using a fixed exchange rate.

one_usd = 283.87
print("Today's rate for one USD in PKR is: ",one_usd)
usd = int(input("Enter amount of USD to convert in PKR: "))
pkr = usd * one_usd
print("The amount for given USD in PKR is: ",float(pkr),"rupees")