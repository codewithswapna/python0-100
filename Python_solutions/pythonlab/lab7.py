#1.Print the first 10 natural numbers using for loop

for i in range(1, 11):
    print(i)


#2.Python program to check if the given string is a palindrome 
def is_palindrome(string):
 
    string = string.replace(" ", "").lower()
    return string == string[::-1]

input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#3.
def is_armstrong(number):
   
    num_str = str(number)
    num_digits = len(num_str)
   
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return number == armstrong_sum

num = int(input("Enter a number: "))

if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

#4.Python program to get the Fibonacci series between 0 to 50 
a, b = 0, 1
print("Fibonacci series between 0 and 50:")

while a <= 50:
    print(a, end=" ")
    a, b = b, a + b


#5.Python program to check the validity of password input by users

import re

def is_valid_password(password):
   
    if (len(password) < 8 or len(password) > 16):
        return "Password must be 8-16 characters long."
    if not re.search("[a-z]", password):
        return "Password must include at least one lowercase letter."
    if not re.search("[A-Z]", password):
        return "Password must include at least one uppercase letter."
    if not re.search("[0-9]", password):
        return "Password must include at least one digit."
    if not re.search("[@#$%^&+=]", password):
        return "Password must include at least one special character (@#$%^&+=)."
    if re.search("\s", password):
        return "Password must not contain spaces."
    return "Valid password."

user_password = input("Enter a password: ")

print(is_valid_password(user_password))