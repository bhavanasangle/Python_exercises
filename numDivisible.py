#4. Write a Python program to check whether a number is divisible by 5 and 11 or not.

num = eval(input('Enter a Number:'))

if num % 5 == 0:
  print("Num is divisible 5")
elif num % 11 == 0:
  print("Num is divisible by 11")
else:
  print('Num is not divisible by 5 & 11')
