#Assinment How to create empty list
a =[]
a
b = list()
b
# to add elements in empty lis we use append
a.append(100)
print(a)

# Assignment : append list,tuple,sl
data =(1,2,3)
data
print(data)

# add above data in a
a.append(data)
print(a)

#add c++
a.append('c++')
print(a)

# append adds a complete object it is
c = [20,20,20]
a.append(c)
print(a)

#use extends() to add individuaal elements
b = [2,3,4]
print(b)

b.extend(data)
print(b)

n = [1,2,3]
m = [5,6,7]

#Q Append vs Extend
# Appends add whole object as it is
# extends adds indivitual element

n.append(m)
print(n)

p = n.extend(m)
print(p)

#To remove elements from list there are two methods

a.pop() # pop removes last element of list
print(a)
a.pop(2) #removes object at index
print(a)

#Removes first occaurence of value
t = [1,2,3,1,1,4]
t.remove(1)
print(t)

#copy the value of object into another one
x = t.copy()
print(x)

#remove all elements
t.clear()
print(t)
