#Q5 Write a function is_strong_password(password) that takes a string.
#It should return True ONLY if the password meets two rules:
#it must be at least 8 characters long AND
#it must contain at least one exclamation point (!).
#Otherwise, return False.

def is_strong_password(password):
  if len(password) >= 8 and "!" in password:
    return "True"
  else:
    return "False"
password = input("Enter a password (Note: Must be 8 characters long and contain an exclamation mark)")
result = is_strong_password(password)
print(f"Password is {result}")