def main():
    amount_due = 50

    # Loop until the amount due is paid off or exceeded
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))

        # Accept only 25, 10, or 5 cent coins
        if coin in [25, 10, 5]:
            amount_due -= coin

    # Calculate change owed if they overpaid
    change_owed = abs(amount_due)
    print(f"Change Owed: {change_owed}")

if __name__ == "__main__":
    main()
