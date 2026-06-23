#Q1
def perimeter(length, width):
  return(2*(length+width))
length = float(input("Length: "))
width = float(input("width: "))
result = perimeter(length, width)
print(f"The perimeter of the rectangle is: {result}")