# BMI CALCULATOR
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

copyright = "Thank you for using AO BMI Calculator. Copyright 2026"
while True:
    print("Welcome to the BMI Calculator!")
    mode = input("Choose a system: Metric(M) or Imperial(I): ").lower()

    if mode == "m":
        weight = float(input("Enter your Weight in kg: "))
        height = float(input("Enter your Height in m: "))
        bmi = round(weight/(height ** 2), 1)
    elif mode == "i":
        weight = float(input("Enter your Weight in pounds(lb): "))
        height = float(input("Enter your Height in Inches(in): "))
        bmi = round(703 * (weight/(height ** 2)), 1)
    else:
        print("Invalid choice. Please enter M or I")
        print("")
        continue

    if bmi < 18.5:
        category = "\033[31mUnderweight\033[0m"
    elif 18.5 <= bmi < 24.9:
        category = "\033[32mHealthy\033[0m"
    elif 25.0 <= bmi <29.9:
        category = "\033[33mOverweight\033[0m"
    else:
        category = "\033[31mObese\033[0m"

    print("BMI Value: ",bmi)
    print("Your Result is: ", category)
    print(copyright)
    again = input("Do you wish to continue: Y/N ").lower()
    if again != "y":
        break
    clear_screen()