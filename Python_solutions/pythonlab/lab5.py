#1.Write a python program to reverse a number using a while loop. 

def reverse_number(number):
    reversed_number = 0
    
    while number > 0:
       
        digit = number % 10
        
        reversed_number = reversed_number * 10 + digit
        
        number = number // 10
    
    return reversed_number

num = 12345
reversed_num = reverse_number(num)
print("Reversed number:", reversed_num)


#2.Write a python program to check whether a number is palindrome or not? 
def is_palindrome(number):
    
    original_number = str(number)
   
    if original_number == original_number[::-1]:
        return True
    else:
        return False

num = 12321
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")


#3.Write a python program finding the factorial of a given number using a while loop. 
def factorial(number):
    
    result = 1
    

    while number > 1:
        result *= number
        number -= 1
    
    return result

num = 5
fact = factorial(num)
print(f"The factorial of {num} is {fact}")


#4.Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.

total_sum = 0


while True:
    
    user_input = int(input("Enter a number (0 to stop): "))
    
   
    if user_input == 0:
        break  
    
   
    total_sum += user_input

print("The sum of all entered numbers is:", total_sum)
