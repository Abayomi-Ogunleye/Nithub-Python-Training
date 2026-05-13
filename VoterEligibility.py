print("WELCOME TO THE VOTERS ELIGIBILITY PAGE")
print("Kindly confirm if you are of age and the right nationality")

voters_age = int(input("Kindly enter your age in Numbers: "))
voters_nationality = input("Are you a Nigerian? yes/no").lower()

if voters_age >= 18 and voters_nationality == "yes":
  print("You are eligible to Vote")
elif voters_age < 18 and voters_nationality == "no":
  print("You are not eligible to Vote")
else:
  print("Enter correct informations and try again")