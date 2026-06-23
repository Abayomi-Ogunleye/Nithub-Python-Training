#Q2
def amount(user_age):
  if user_age <= 12:
    return (f"${10}")
  else:
    return (f"${15}")
user_age = int(input("Enter your age: "))
price = amount(user_age)
print(f"The price is {price}")
