amount_due = 50
while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    Insert_coin =int(input("Insert Coin: "))
    if Insert_coin >=30:
        continue
    elif amount_due >= 0:
        amount_due -= Insert_coin
        continue
    else:

        break
print(f"Change Owed: {abs(amount_due)}")
