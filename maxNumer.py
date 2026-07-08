#1. Write a Python program to find maximum between two numbers.

num1 = input('Enter First Number:')
num2 = input('Enter Second Number:')

if num1 > num2:
    print(num1 + ' Num1 is greater than Num2 ' + num2)
elif num2 > num1:
    print(num2 + ' Num2 is greater than Num1 ' + num1)
else:
    print(num1 + ' and ' + num2 + ' are equal')
