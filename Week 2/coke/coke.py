def main():
    total = 0
    while total <50:
        bal = 50 - total
        print(f"Amount Due: {bal}")
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5 :
            total += coin
    if total >= 50:
        print(f"Change Owed: {(total-50)}")
main()
