# No match:


def birthday_noclash(n):
    '''return the probability of no clash in a group of n birthdays'''
    p=1
    for i in range(n):
        p=p*((365-i)/365)
    return p

birthday_noclash(23)

for n in range(40):
    print (n,birthday_noclash(n))

import random
classSize = 23
birthdayList = []

for i in range(classSize):
    newBDay = random.randrange(365)
    birthdayList.append(newBDay)

print(birthdayList)


import random
classSize = 23
numTrials = 1000
dupeCount = 0

for trial in range(numTrials):
    birthdayList = []
    for i in range(classSize):
        newBDay = random.randrange(365)
        birthdayList.append(newBDay)

    foundDupe = False
    for num in birthdayList:
        if birthdayList.count(num) > 1:
           foundDupe = True

    if foundDupe == True:
        dupeCount = dupeCount + 1

prob = dupeCount / numTrials
print("The probability of a shared birthday in a class of ", classSize, " is ", prob)



dates = [(3,14),(2,8),(10,25),(5,17),(3,2),
         (7,25),(4,30),(8,7),(2,8),(1,22)]

sorted(dates)

sorted(((dates.count(e), e) for e in set(dates)), reverse=True)


dates.pop()

for count, elem in sorted(((dates.count(e), e) for e in set(dates)), reverse=True):
    print('{} {:d}'.format(elem, count))

##
dates = [(3,14),(2,8),(10,25),(5,17),(3,2),
         (7,25),(4,30),(8,7),(2,8),(1,22)]
count=0
n=0
while n<len(dates)-1:
    if sorted(dates)[n+1]==sorted(dates)[n]:
        count+=1
    n+=1

print("Total birthday pairs:", count)
##
set(dates)

for l1, l2 in zip(dates, dates[1:]):
    print(l1, l2)
##
for l1, l2 in zip(sorted(dates), sorted(dates[1:])):
    if l1[1]==l2[1]:
        print(l1, l2)
##
dates = [(3,14),(2,8),(10,25),(5,17),(3,2),
         (7,25),(4,30),(8,7),(2,8),(1,22)]
sorted(dates)
##
import numpy as np
map(dates,np.array)

type(dates[1])



# You can use a similar approach to actually retrieve the duplicates.

s = set()
duplicates = set(x for x in dates if x in s or s.add(x))
duplicates

s.add((2,8))

sorted(dates)


##
import random
# 生成数列，一万个数
arr_length = 10001
list=[i for i in range(1, arr_length)]

rnd = random.randrange(1, arr_length)
list.insert(rnd - 2, rnd)
print('\n重复数为：' + str(rnd))
print('\n开始查找')
left = 0
right = arr_length
count = 0
while ((right - left) > 1) and count <100:
    pos = (left + right) // 2
    count = count + 1
    print('第 %d 次定位：%d' % (count, pos))
    count+=1
    if (list[pos] == pos):
        right = pos
    else:
        left = pos

print('\n查找结果：', list[left])
##
list=sorted(dates, key=lambda x: sum(x))
left=0
right=len(dates)-1
count=0
while right!=left and count<5:
    count += 1
    pos=len(dates)//2
    print('第 %d 次定位：%d' % (count, pos))
    if (list[pos] == pos):
        right=pos
    else:
        left=pos

print('\n查找结果：', list[left])

##
# Function to print duplicates


def printRepeating(arr, size):
    print("The repeating elements are: ")

    for i,v in enumerate(arr):

        if v > (0,0):
            print(arr[i])
            arr[i] = (0,0)
            print(arr[i])
        else:
            print(arr[i], end=" ")

        # Driver code


arr = [(3,14), (2,8), (10,25), (5,17), (3,2),
       (7,25), (4,30), (8,7), (2,8), (1,22)]
arr_size = len(arr)

printRepeating(arr, arr_size)
arr[1]

a=(2,8)
arr = [1, 2, 3, 1, 3, 6, 6]
# This code is contributed by Shreyanshi Arun.
##

deposits = [(0, 4, .3), (6, 2, 3), (3, 7, 2.2), (5, 5, .5), (3, 5, .8), (7, 7, .3)]

l=[]
for i in range(0,len(deposits)):
    l.append(deposits[i][:2])

print (l)


board=np.empty([8, 8], dtype="<U10")
board[:]="-"

for i in l:
    board[i[0],i[1]]="x"

board[0:8,0:8]
board[5:8,5:8]





for i in board:
    print("".join(i.tolist()))

##
tweets = ["This is great! RT @fake_user: Can you believe this?",
         "It's the refs! RT @dubsfan: Boo the refs and stuff wargarbal",
         "That's right RT @ladodgers: The dodgers are destined to win the west!",
         "RT @sportball: That sporting event was not cool",
         "This is just a tweet about things @person, how could you",
         "RT @ladodgers: The season is looking great!",
         "RT @dubsfan: I can't believe it!",
         "I can't believe it either! RT @dubsfan: I can't believe it"]
##
import re
from collections import Counter
d={}
ans=Counter([re.search(r"@(.*?):",i).group(1) for i in tweets if re.search(r"@(.*?):",i)])
type(ans)
for k, v in ans.items():
    d[k] = v
print (d)
##
mystring =  "hi my name is ryan, and i am new to python and would like to learn more"
keyword = 'name'
befor_keyowrd, keyword, after_keyword = mystring.partition(keyword)


d1 = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
d2 = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

d2=d1
d1.pop(1)
d2
print ("dd")

##

