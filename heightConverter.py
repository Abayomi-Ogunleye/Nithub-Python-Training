#Feet to Centimeters: feet * 30.48
#Inches to Centimeters: inches * 2.54
#Centimeters to Feet: cm / 30.48
#Centimeters to Total Inches: cm / 2.54

print("""Welcome to LBKE Height converter
You can convert the following:
1. Feet(Ft'In) to Centimeter
2. Inches to Centimeter
3. Centimeters to Feet
4. Centimeters to Total Inches""")

while True:
  menu = input("Enter the corresponding number above to convert: ")

  if menu == "1":
    feet = float(input("Enter the Height in feet: "))
    inches = float(input("Enter the height in inches: "))
    FtoC = float(((feet*12) + inches)*2.54)
    print(f"Your height is {FtoC} Centimeters")
  elif menu == "2":
    inches = float(input("Enter the height in Inches: "))
    ItoC = float(inches*2.54)
    print(f"Your height is {ItoC} centimeters")
  elif menu == "3":
    centi = float(input("Enter the height in Centimeters: "))
    CtoF = float(centi/30.48)
    print(f"Your height is {round(CtoF,2)} feet")
  elif menu == "4":
    centi = float(input("Enter the height in Centimeters: "))
    CtoI = float(centi/2.54)
    print(f"Your height is {round(CtoI,2)} inches")
  else:
    print("Enter a valid value from 1 t0 4")
  loop = input("Do you wish to continue? Y/N ")
  if loop.lower() != "y":
    break
