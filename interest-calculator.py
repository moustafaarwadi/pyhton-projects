import math
principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the principal amount of money: "))
    if principal <= 0:
        print("The principal can't be less then or equal to zero!")
while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("The interest rate can't be less then or equal to zero!")
while time <= 0:
    time = float(input("Enter the number of years: "))
    if time <= 0:
        print("The number of years can't be less then or equal to zero!")
total = principal * math.pow((1 + rate/100), time)
formatted_total = "{:.2f}".format(total)
print(f"the total amount of money during {time} years is ${formatted_total}")