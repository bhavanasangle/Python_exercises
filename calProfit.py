#Write a Python program to calculate profit or loss. Input is selling cost and actual cost.

sellCost = float(input('Enter Selling cost of item'))
actulCost = float(input('Enter Actual cost of item'))

if sellCost > actulCost:
  profit = sellCost - actulCost
  print('Your total profit is :', profit)
else:
  loss = actulCost - sellCost
  print("Your total loss is :",loss)
