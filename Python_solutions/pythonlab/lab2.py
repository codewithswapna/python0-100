#1.Using input() function take one number from the user and using ternary operators check whether the number is even or odd

num = int(input("Enter a number: "))
result = "Even" if num % 2 == 0 else "Odd"
print(f"The number is {result}.")


#2.Using input function take two number and then swap the number 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num1, num2 = num2, num1
print(f"After swapping: First number = {num1}, Second number = {num2}")


#3.Write a Program to Convert Kilometers to Miles
kilometers = float(input("Enter distance in kilometers: "))
kilometers_to_miles = 0.621371
miles = kilometers * kilometers_to_miles
print(f"{kilometers} kilometers is equal to {miles} miles.")


#4.Find the Simple Interest on Rs. 200 for 5 years at 5% per year.
P = 200 
R = 5    
T = 5 

SI = (P * R * T) / 100
print(f"The Simple Interest is Rs. {SI}")