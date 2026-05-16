balance = 100000
user_pin = 1234
copyright = "Thank you for using AO bank. Copyright 2026"


while True:
    print("ATM SIMULATOR")
    print("To continue banking, enter a pin for transactions")

    print("Choose transaction type: ")
    t_type = int(input("1.Withdraw 2.Deposit 3.Check Balance 4.Exit "))
    if t_type == 1:
        amount = float(input("Enter amount to Withdraw: "))
        t_pin = int(input("Enter Transaction PIN: "))
        if amount <= balance and user_pin == t_pin:
            print("You have successfully withdrawn",amount)
            balance = balance-amount
            print("Current balance: ", balance)
        else:
            print("Insufficient balance or invalid pin")
        print(copyright)
        another = input("Do you wish to perform another transaction? (Y/N) ").lower()
        if another != "y":
            break
    elif t_type ==2:
        d_amount = float(input("Enter amount to Deposit: "))
        t_pin = int(input("Enter Transaction PIN: "))
        if t_pin == user_pin:
            print("You have successfully deposited",d_amount)
            balance = balance+d_amount
            print("Current balance: ", balance)
        else:
            print("Incorrect pin")
        print(copyright)
        another = input("Do you wish to perform another transaction? (Y/N) ").lower()
        if another != "y":
            break
    elif t_type == 3:
        t_pin = int(input("Enter Transaction PIN: "))
        if t_pin == user_pin:
            print("Your current balance is: ", balance)
        else:
            print("Incorrect pin")
        print(copyright)
        another = input("Do you wish to perform another transaction? (Y/N) ").lower()
        if another != "y":
            break
    elif t_type == 4:
        print(copyright)
        break
    else:
        print("Invalid Transaction")
        print(copyright)
