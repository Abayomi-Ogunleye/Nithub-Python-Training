#Q3 Write a function is_valid_username(username) that takes a
#string. It should return True if the username is at least 6
#characters long, and False if it is shorter

def is_valid_username(username):
  if len(username) >= 6:
    return f"True"
  else:
    return f"False"
username = input("Username: ")
output = is_valid_username(username)
print(output)