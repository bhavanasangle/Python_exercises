#2. Write a Python program to find maximum among three numbers.

#Using max of num
nums = [float(input(f"Enter {i}: ")) for i in range(1, 4)]
# Use max()
print(f"Max: {max(nums)}")

num1 = eval(input('Enter First Number:'))
num2 = eval(input('Enter Second Number:'))
num3 = eval(input('Enter Third Number:'))

if num1 >= num2 and num1 >= num3:
    print('Num1 is greater',num1)
elif num2 >= num1 and num2 >= num3:
    print('Num2 is greater',num2)
else:
    print('Num3 is greater',num3)

