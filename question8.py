#Question No 8
# Calculate Profit or Loss
# Input cost price and selling price. Display either:
# Profit and amount, or
# Loss and amount, or
# No Profit No Loss

#let's put a check so that user do not enter amount less than zero
cp = 0
sp = 0
while cp <= 0 or sp <= 0:
      cp = int(input("Enter the Cost Price: "))
      sp = int(input("Enter the Selling Price: "))
      if cp <= 0 or sp <= 0:
           print("Enter a valid amount greater than zero for either values.")

print("The cost price is: ", cp)      
print("The selling price is: ", sp)
      

if cp == sp:      #first check if both amount are same
    print("There is no profit no loss.")
elif cp > sp:
    loss = cp - sp       #loss formula
    print("Loss amount is: ", loss)
else:
    profit = sp - cp     #profit formula
    print("Profit amount is: ", profit)