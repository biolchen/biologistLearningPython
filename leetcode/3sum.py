
##
nums = [-1, 0, 1, 2, -1, -4]

import itertools
class Solution:
        def twoSum(self, nums, target):
            i=0
            nums = sorted(nums)
            j=len(nums)-1
            ans = []
            while i<j:
                sum = nums[i]+nums[j]
                if sum<target:
                    i+=1
                    continue
                if sum>target:
                    j-=1
                    continue
                if nums[i]+nums[j]==target:
                    if [nums[i],nums[j]] not in ans:
                        ans.append([nums[i],nums[j]])
                    i+=1
                    j-=1
            return ans

        def threeSum(self, nums):
            from collections import defaultdict
            nums = sorted(nums)
            d=defaultdict()
            ans=[]
            for i in range(0,len(nums)):
                target0=nums.pop(0)*(-1)
                l = self.twoSum(nums, target0)
                if len(l)>0: 
                    if target0*-1 not in d:
                        d[target0*-1]=l
            for k,v in d.items():
                ans+=(list(map(lambda x: [k]+x, v)))
            return ans

Solution().threeSum(nums)
##
nums = [-2,0,1,3]
target = 2


class Solution:
        def threeSumSmaller(self, nums, target):
            nums.sort()
            print(nums)
            res = 0
            l = []
            for k in range(len(nums)):
                i=0
                j=k-1
                while i<j:
                    if nums[i] + nums[j] + nums[k] < target:
                        l.append([i,j,k])
                        res+=j-i
                        i+=1
                    else:
                        j-=1
            return res
Solution().threeSumSmaller(nums, target)
##
nums = [-1, 2, 1, -4]
nums = [0,2,1,-3]
target = 1

class Solution:
        def threeSumClosest(self, nums, target):
            nums.sort()
            print(nums)
            result = nums[0] + nums[1] + nums[2]
            for i in range(len(nums)-2):
                j, k = i+1, len(nums) - 1
                while i< j < k:
                    SUM = sum([nums[i],nums[j],nums[k]])
                    if SUM == target:
                        return SUM
                    if abs(SUM-target) < abs(result-target):
                        result = SUM
                    if SUM<target:
                        j+=1
                    if SUM>target:
                        k-=1
            return result

Solution().threeSumClosest(nums,target)

##

Input=[1,3,5,6]
target = 5
import numpy as np
class Solution:
        def searchInsert(self, nums, target):
            try:
                ans = np.max(np.where(np.array(sorted(nums))<target))+1
            except ValueError:
                return 0
Solution().searchInsert(Input, target)
##
            
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
nums1[:m]
nums1[m:]
class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1[:] = sorted(nums1[:m]+nums2)

##
A = ["bella","roller","label"]
from collections import Counter
class Solution:
    def commonChars(self, A):
        res = Counter(A[0])
        for a in A:
            print(a)
            res &= Counter(a)
            print(res)
        return list(res.elements())

Solution().commonChars(A)

##
'''
题目中的Follow up让我们在O(n^2)的时间复杂度内实现，那么我们借鉴之前那两道题3Sum Closest和3Sum中的方法，采用双指针来做，这里面有个trick就是当判断三个数之和小于目标值时，此时结果应该加上right-left，以为数组排序了以后，如果加上num[right]小于目标值的话，那么加上一个更小的数必定也会小于目标值，然后我们将左指针右移一位，否则我们将右指针左移一位，参见代码如下：
'''

nums = [-2,0,1,3]
nums = [3,1,0,-2]
target = 4

class Solution:
    def threeSumSmaller(self, nums, target):
        nums.sort()
        count = 0
        for k in range(len(nums)):
            i=0
            j=k-1
            while i<j:
                SUM = nums[i]+nums[j]+nums[k]
                if SUM<target:
                    count += j-i
                    i+=1
                if SUM>=target:
                    j-=1
        return count
Solution().threeSumSmaller(nums, target)
##

S='aaaba'

class Solution:
    def countLetters(self, S):
        pre = 'A'
        l = 0
        ans = 0
        for i in range(len(S)):
            print(S[i],l)
            if S[i]!=pre:
               ans += int(l*(l+1)/2)
               pre=S[i]
               l=1
            else:
               l+=1
        ans+=int(l*(l+1)/2)
        return ans
            
Solution().countLetters(S)

##
nums = [9,6,4,2,3,5,7,0,1]
class Solution:
    def missingNumber(self, nums):
        return (set(range(len(nums)+1))-set(nums)).pop()
        
Solution().missingNumber(nums)
##

s = "abcd"
t = "abcde"
l = list(s)+list(t)
l
t.count('a')
from functools import reduce
reduce(lambda x,y:x^y, list(s)+list(t))
s = 'a'
t = 'aa'
set(s)+set(t)
if set(t)
set(t)-set(s)

##
from collections import Counter
Input = ["bella","label","roller"]
Input = ["cool","lock","cook"]
a = Counter(Input[0])
b = Counter(Input[1])
c = Counter(Input[2])
print(a)
print(b)
print(c)
a & b
a & c
print(a)

##
Input = ["cool","lock","cook"]
Input = ["bella","label","roller"]
from collections import Counter
class Solution:
    def commonChars(self, A):
        res = Counter(A[0])
        for i in A:
            res &= Counter(i)
        return list(res.elements())

Solution().commonChars(Input)

##
s = "a"
t = "ab"

a = Counter(s)
b = Counter(t)
b-a
len(a-b)
b
##
s = "cbaebabacd" 
p = "abc"
from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        ans = []
        C = Counter(p)
        window = None
        for i in range(len(s)-len(p)+1):
            if i==0:
                window = Counter(s[i:i+len(p)])
                print(window)
            else:
                minus = {s[i-1]:1}
                plus = {s[i+len(p)-1]:1}
                print("minus:{}; plus:{}".format(minus, plus))
                window -= minus
                window += plus
                print(window)
            if C==window: ans.append(i)
        return ans

Solution().findAnagrams(s,p)
##


  


      
##
