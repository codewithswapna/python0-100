#1. Python program to check if a year is a leap year

def is_leap_year(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True 
            else:
                return False  
        else:
            return True 
    else:
        return False  


year = int(input("Enter a year: "))


if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#2.Python program to find the largest among three numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))


if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is {largest}.")

#3.Python program to check if a number is positive, negative, or zero

num = float(input("Enter a number: "))

if num > 0:
    print(f"{num} is a positive number.")
elif num < 0:
    print(f"{num} is a negative number.")
else:
    print("The number is zero.")


#4.Python program to calculate the net amount after discount for toy orders

product_code = int(input("Enter the product code (1 for Battery Based, 2 for Key Based, 3 for Electrical Charging Based): "))
order_amount = float(input("Enter the order amount: "))

discount = 0

if product_code == 1: 
    if order_amount > 1000:
        discount = 0.10 * order_amount
elif product_code == 2:  
    if order_amount > 100:
        discount = 0.05 * order_amount
elif product_code == 3:  
    if order_amount > 500:
        discount = 0.10 * order_amount
else:
    print("Invalid product code!")

net_amount = order_amount - discount

print(f"Order amount: Rs. {order_amount:.2f}")
print(f"Discount applied: Rs. {discount:.2f}")
print(f"Net amount to pay: Rs. {net_amount:.2f}")


#5.Python program to calculate fare based on distance

distance = float(input("Enter the distance traveled (in km): "))

fare = 0

if 1 <= distance <= 50:
    fare = distance * 8
elif 51 <= distance <= 100:
    fare = distance * 10
elif distance > 100:
    fare = distance * 12
else:
    print("Invalid distance entered!")

if fare > 0:
    print(f"The fare for {distance} km is Rs. {fare:.2f}")
