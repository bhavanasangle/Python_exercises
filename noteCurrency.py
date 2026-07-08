#10.Write a Python program to count total number of notes in given amount
amount = int(input('Enter your amount :'))

currency = [500,100,50,20,10,5,1]
notes = {}

#notes[currency[0]]= amount / currency[0]


for i in currency:
  newAmount = amount % i
  if int(amount / i) > 0 :
    notes[i] = int(amount / i)
    amount = newAmount

print("Notes", notes) 



#using while loop


"""i = 0

while amount > 0 :
 
  newA = amount % currency[i]
  if int(amount / currency[i]) > 0 :
    notes[currency[i]] = int(amount / currency[i])
  amount = newA
  i = i + 1 """


print("Done")
