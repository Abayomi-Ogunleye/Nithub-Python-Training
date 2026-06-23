#7

pwd = "much"
user_pwd = input("Enter your password: ")
while pwd != user_pwd:
  print("Incorrect password")
  user_pwd = input("Enter your password: ")
print("Access Granted")