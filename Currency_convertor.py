with open("currency_data.txt") as f:
    lines = f.readlines()

currencyDict = {}
currencyDictINR = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]]= parsed[1]
    currencyDictINR[parsed[0]] = parsed[2]

# print(currencyDict)
# print(currencyDictINR)
# print("\n")
print("Please choose the currency option below:-\n"
      "options 1 : INR to Others Currency\n"
      "options 2 : Others Currency to INR")
option = int(input())
if option == 1:
    print("Enter the amount:")
    amount = float(input())
    [print(item) for item in currencyDict.keys()]
    print("\nEnter the currency name from top available list")
    currency = input()
    print(f"{amount} INR is equal to {amount*float(currencyDict[currency])} {currency}")
else:
    print('Enter the amount:')
    amount = float(input())
    [print(item) for item in currencyDictINR.keys()]
    print("\nEnter the currency name from top available list")
    currency = input()
    print(f"{amount} {currency} is equal to {amount*float(currencyDictINR[currency])} INR")

