
'''
heappush(heap, item): 将item压入堆数组heap中。
必须先进行此步操作,后面的heappop才有效。
heappop(heap): 从堆数组heap中取出最小的值,并返回。
'''

import heapq as hq

a=[1, 3, 7, 3, 2, 10, 9]
h = []
for i in a:
    hq.heappush(h, i)
print ([hq.heappop(h) for i in range(len(h))])


def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]

a=[1, 3, 7, 3, 2]
heapsort(a)
heappush(a,120)

##########
heap = []
heappush(heap,7)
heap

data = [100,203, 1, 3, 5, 7, 9, 4, 6, 8, 0]
heapify(data)
a=[]
for i in range(0,len(data)):
    a.append(heappop(data))
print(a)
###########

heappop(data)

for item in data:
     heappush(heap, item)

heappop(heap)

ordered = []
while heap:
    ordered.append(heappop(heap))
ordered
data.sort()
data == ordered

'''
heappushpop(heap, item)
增加item的同时删除最小值,并且返回该堆的最小值
'''
def example(iterable):
    h = []
    for value in iterable:
        hq.heappush(h, value)
    a = hq.heappop(h)
    # 增加4的同时删除最小值,并且返回该最小值
    b = hq.heappushpop(h, 4)
    print (a)
    print (b)
    print (h)

a
heappushpop(a, 4)

'''
heapify(x)
x必须是list，此函数将list变成堆，实时操作。从而能够在任何情况下使用堆的函数。
'''
import heapq as hq

def example2(iterable):
    h = []
    for i in iterable:
        hq.heappush(h, i)
    hq.heapify(h)
    print(h)

a = [100,203, 1, 3, 5, 7, 9, 23,4, 6, 8, 0]
example2(a)


'''
heapreplace(heap, item)
先进行删除,后压入栈
'''
a = []
hq.heappush(a, 3)
# 输出: [3]
print (a)
# 先执行删除（heappop(a)->3),再执行加入（heappush(a,4))


hq.heapreplace(a, 4)
# 输出: [4]
print (a)

data = [100,203, 1, 3, 5, 7, 9, 4, 6, 8, 0]
hq.heapify(data)
hq.heappop(data)
hq.heappushpop(data, 40000)
data
'''
归并排序
merge(*iterables)
'''

a = [2,4,6]
b = [1,3,5]
c = hq.merge(a, b)
# 输出: [1, 2, 3, 4, 5, 6]
list(c)

'''
nlargest(n, iterable[, key]), nsmallest(n, iterable[, key])
获取列表中最大、最小的几个值。
'''

a = [1, 3, 4, 2]
# 输出: [4, 3]
hq.nlargest(2, a)
# 输出: [1, 2]
hq.nsmallest(2, a)


############
############

'''
leetcode上面的题目：

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

我之前不用heap的解法（耗时200ms)…当时对heap模块不了解
'''

import numpy as np
mm = np.matrix([])
mm
mm = np.append(mm, [[1,2]], axis=1)
mm

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        arr = []
        for item in matrix:
            for son in item:
                arr.append(son)
        arr = sorted(arr)
        return arr[k-1]

# 后来看了discussion里面的做法，恍然大悟…(这个方法耗时180ms）

class Solution2(object):
    def kthSmallest(self, matrix, k):
        result, heap = None, []
        heapq.heappush(heap, (matrix[0][0], 0, 0))
        while k > 0:
            result, i, j = heapq.heappop(heap)
            if i == 0 and j + 1 < len(matrix):
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
            if i + 1 < len(matrix):
                heapq.heappush(heap, (matrix[i+1][j], i+1, j))
            k -= 1
        return result

# python cookbook example 1
#
# Example of using heapq to find the N smallest or largest items

import heapq as hq

portfolio = [
   {'name': 'IBM', 'shares': 100, 'price': 91.1},
   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
   {'name': 'FB', 'shares': 200, 'price': 21.09},
   {'name': 'HPQ', 'shares': 35, 'price': 31.75},
   {'name': 'YHOO', 'shares': 45, 'price': 16.35},
   {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = hq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = hq.nlargest(3, portfolio, key=lambda s: s['price'])

print(cheap)
print(expensive)

# python cookbook example 2
#
# Example of a priority queue

import heapq as hq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        hq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return hq.heappop(self._queue)[-1]
# Example use
class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

print("Should be bar:", q.pop())
print("Should be spam:", q.pop())
print("Should be foo:", q.pop())
print("Should be grok:", q.pop())




a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in hq.merge(a, b):
    print(c)



# for loop in python

x = 1
while x < 100:
    print("To infinity and beyond! We're getting close, on %d now!" % (x))
    x += 1

for x in range(1, 11):
    for y in range(1, 11):
        print ('%d * %d = %d' % (x, y, x*y))

for x in range(0, 3):
    print("We're on time %d" % (x))





import heapq as hq

def heapsort(iterable):
    h = []
    for value in iterable:
        hq.heappush(h, value)
    return [hq.heappop(h) for i in range(len(h))]

a=[1, 3, 7, 3, 2]
heapsort(a)
hq.heappush(a,120)
a

a=[1, 3, 7, 3, 2,10,9]
h = []
for i in a:
    hq.heappush(h, i)
print([hq.heappop(h) for i in range(len(h))])

heap = []
hq.heappush(heap,7)
heap

data = [100,203, 1, 3, 5, 7, 9, 4, 6, 8, 0]
hq.heapify(data)

hq.heappop(data)

a=[]
for i in range(0,len(data)):
    a.append(hq.heappop(data))


heapsort(data)
hq.heappop(data)
a.append(1)
a

class tes:
    def orderxxx(self,num):
        list1=[]
        while True:
            n=num
            if n==0:
                break
            else:
                list1.append(n)
        list1.sort()
        print(list1)


    help(hq.nlargest)

dir(tes)

a=[1023230,123,12,3]
len(a)
for i in range(1,len(a)):
    #for j in range(1,len(a)-1):
    print ((hq.nlargest(1,a)))


hq.nlargest(3, a)

dir(hq)

hq.nlargest(1,a)
hq.heapify(a)
hq.heappop(a)
list=[]


