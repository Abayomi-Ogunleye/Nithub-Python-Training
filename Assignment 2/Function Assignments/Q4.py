#Q4 Write a function that takes an integer. It should return the
#string "Even" if the number is even, and "Odd" if the number is odd.

def even_number(number):
  if number%2 != 0:
    return "Odd"
  else:
    return "Even"
number = int(input("Enter a Number: "))
result = even_number(number)
print(f"The number is {result}")