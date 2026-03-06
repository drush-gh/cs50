amountDue = 50

while amountDue > 0:
    coin = int(input("Insert coin: "))
    if coin not in [5, 10, 25]:
        print("Amount Due:", amountDue)
    else:
        amountDue -= coin
        if amountDue > 0:
            print("Amount Due:", amountDue)
        else:
            break

print("Change Owed:", abs(amountDue))
