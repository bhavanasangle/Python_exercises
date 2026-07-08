# 11. Write a Python program to input all sides of a triangle and check whether
#triangle is valid or not

sizeA = float(input("Enter first length of trangle"))
sizeB = float(input('Enter second length of trangle'))
sizeC = float(input('Enter third length of trangle'))

if (sizeA <= 0) or (sizeB <= 0) or (sizeC <= 0):
  print('Please enter valid lenghths of trangle')
else:
  if (sizeA + sizeB > sizeC) and (sizeA + sizeC > sizeB) and (sizeB + sizeC > sizeA) :
    print("Its a valid triangle")
  else:
    print("Invalid tringle! Sum of two sides of trangle must be greter than one side")

