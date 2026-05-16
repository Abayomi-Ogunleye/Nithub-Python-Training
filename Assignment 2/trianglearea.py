import math

print("Area of a Triangle Calculator")
triangle_type = int(input("Choose a triangle type: 1.Equilateral 2.Isosceles 3.Scalene 4.Right-angle 5.Any Triangle: "))

if triangle_type == 1:
    e_side= float(input("Enter the length of the side: "))
    print("Area of Equilateral Triangle: ",round((math.sqrt(3)/4) * e_side ** 2, 3))
    print("Copyright 2026, Ogunleye Abayomi A.")
elif triangle_type == 2:
    base = float(input("Enter the base length: "))
    i_side = float(input("Enter the equal side length: "))
    print("Area of Isosceles Triangle: ", round((base/4) * math.sqrt(4 * i_side ** 2 - base ** 2), 3))
    print("Copyright 2026, Ogunleye Abayomi A.")

elif triangle_type == 3:
    base = float(input("Enter the base length: "))
    height = float(input("Enter height length: "))
    print("Area of Scalene triangle: ", round((1/2) * base * height, 3))
    print("Copyright 2026, Ogunleye Abayomi A.")

elif triangle_type == 4:
    base = float(input("Enter the base length: "))
    height = float(input("Enter height length: "))
    print("Area of Right-angle triangle: ", round((1/2) * base * height, 3))
    print("Copyright 2026, Ogunleye Abayomi A.")

elif triangle_type == 5:
    side_a = float(input("Enter the value for side a: "))
    side_b = float(input("Enter the value for side b: "))
    side_c = float(input("Enter the value for side c: "))
    s = (side_a + side_b + side_c) / 2
    print("Area of the triangle: ", round(math.sqrt(s*(s-side_a)*(s-side_b)*(s-side_c)), 3))
    print("Copyright 2026, Ogunleye Abayomi A.")


else:
    print("Kindly pick a valid answer and try again")
    print("Copyright 2026, Ogunleye Abayomi A.")
    