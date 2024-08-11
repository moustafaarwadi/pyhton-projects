import math

radius = float(input("enter the radius of the circle (in cm): "))
circumference = 2 * radius * math.pi
area = math.pi * radius * radius 

print(f"the circumference is {round(circumference, 2)} cm")
print(f"the area is {round(area, 2)} cm^2")