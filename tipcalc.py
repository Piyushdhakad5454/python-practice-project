def tip_calculator():
    bill = float(input("Enter the total bill amount: "))
    tip_percentage = float(input("Enter the tip percentage: "))
    tip = (tip_percentage / 100) * bill
    total = bill + tip
    print(f"Tip: ${tip:.2f}")
    print(f"Total amount: ${total:.2f}")

tip_calculator()
