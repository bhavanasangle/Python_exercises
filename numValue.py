'''**3. Write a Python program to check whether a number is
negative, positive or zero.**'''
num = eval(input('Enter Number :'))

if num > 0:
  print('Given Number is Positive', num)
elif num < 0:
  print('Given Number is Negative', num)
else:
  print('Given Number is zero', num)

