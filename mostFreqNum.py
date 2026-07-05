# Assignment:
# k = [1,1,1,2,2,3,4,5]
# I want to fetch most frequent numbers from the list

k = [1,1,1,2,2,3,4,4,4,4,5]
s1 = set(k)
dict1 = {}

for n in s1:
  dict1[n] = k.count(n)
  #dict1.setdefault(n,k.count(n))
print(dict1)

maxNum = dict1.values()
print(max(maxNum))

for key, val in dict1.items():
    if val == max(maxNum):
        print(key)

############
k = [1,1,1,2,2,3,4,5]
max_count = 0

for num in k:
  count = k.count(num)
  if count > max_count:
    max_count = count
    max_num = num

print(max_num)
##############
# Assignment:
# k = [1,1,1,2,2,3,4,5]
# I want to fetch most frequent numbers from the list

k = [1,1,1,2,2,3,4,5,4,4,4]
s1 = set(k)
dict1 = {}

for n in s1:
  dict1[n] = k.count(n)
  #dict1.setdefault(n,k.count(n))

maxNum = max(dict1.values())
print(dict1)
for key, val in dict1.items():
    if val == maxNum:
        print(key)
        maxNum = maxNum-1

