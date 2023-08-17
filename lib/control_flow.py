#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username=="admin" and password=="12345" or username=="ADMIN" and password=="12345":
        print("Access granted")
        return "Access granted"
    else:
        print("Access denied")
        return "Access denied"
       
admin_login("ADMIN","12345")

def hows_the_weather(temperature):
    # your code here
    if temperature<40:
        print( "It's brisk out there!")
        return  "It's brisk out there!"
    elif temperature<65:
        print("It's a little chilly out there!")
        return "It's a little chilly out there!"
    elif temperature>85:
        print("It's too dang hot out there!")
        return "It's too dang hot out there!"
    else:
        print("It's perfect out there!")
        return "It's perfect out there!"
hows_the_weather(67)    

def fizzbuzz(num):
    # your code here
    if num % 3==0 and num % 5==0:
        print("FizzBuzz")
        return "FizzBuzz"
    elif num % 3==0:
        print("Fizz")
        return "Fizz"
    elif num % 5==0:
        print("Buzz")
        return "Buzz"
    else:
        print (num)
        return num
fizzbuzz(15)    

def calculator(operation, num1, num2):
    # your code here
    if operation== "+":
        print(num1+num2)
        return num1+num2
    elif operation=="-":
        print(num1-num2)
        return num1-num2
    elif operation=="*":
        print(num1*num2)
        return num1*num2
    elif operation=="/":
        print(num1/num2)
        return num1/num2
    else:
        print("Invalid operation!")
        return None
calculator("+",7,4)
# def calculator_mapping(operation,num1,num2):
#     dict_operations={
#         "+": num1+num2,
#         "-": num1-num2,
#         "*":num1*num2,
#         "/":num1/num2,
#     }
#     result= dict_operations.get(operation,"Invalid operation!")
#     print(result)
#     return result
# calculator_mapping("+",7,3)