'''
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

'''
##
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type: str
        :rtype:int
        """
        import numpy as np
        char_d = {}
        start = 0
        maxL = 0
        curL = 0
        for i,v in enumerate(s):
            if v not in char_d:
                char_d[v]=i
                print(char_d)
                curL+=1
            else:
                maxL = curL if curL > maxL else maxL
                start = char_d[v]+1


        return ansIndex

Input= "ddabcabcbb"
Solution().lengthOfLongestSubstring(Input)
##
class Solution:
    def longestPalindrome(self, s):
        k = 1
        maxLen = 1
        ans = ''
        while k <= len(s):
            for i in range(len(s)):
                kmer = s[i:i+k]
                if kmer[::-1] == kmer and len(kmer) >= maxLen:
                    maxLen = len(kmer)
                    ans=kmer
            k+=1
        return ans

Solution().longestPalindrome('babad')


##
inputs = [[],[1],[100],[3001],[3002]]

class RecentCounter:
    from collections import deque
    def __init__(self):
        self.q = deque()

    def ping(self, t):
        self.q.append(t)
        try:
            while self.q[0] < 3000:
                self.q.popleft()
        except IndexError:
            pass
        return len(self.q)

t = 3001
obj = RecentCounter()
param_1 = obj.ping(t)
print(param_1)
##

class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        """
        from collections import deque
        import numpy as np
        self.maxLen = size
        self.d = deque()

    def next(self, val):
        self.d.append(val)
        if len(self.d) > self.maxLen:
               self.d.popleft()
        return np.mean(self.d)

m = MovingAverage(3)
m.next(1)
m.next(10)
m.next(3)
m.next(5)
##


##
from collections import deque
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = deque()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.stack.popleft()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack
##
a = MyQueue()
a.push(1)
a.pop()
a
##

from collections import deque

class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.stack.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.stack
##



class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(j for i,j in enumerate(sorted(nums)) if i%2==0)

##
import numpy as np
class Solution:
     def sortArrayByParityII(self, A):
        res = np.zeros(len(A), dtype='int32')
        odd, even = 1,0
        for number in A:
            if number%2==0:
                res[even] = number
                even += 2
            else:
                res[odd] = number
                odd += 2
        return list(res)

Solution().sortArrayByParityII([4,2,5,7])
##
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

class Solution:
    def relativeSortArray(self, arr1, arr2):
        return sorted((x for x in arr1 if x in arr2), key=arr2.index) + sorted([x for x in arr1 if x not in arr2])

Solution().relativeSortArray(arr1,arr2)
##

class Solution:
    def fib(self, N):
        if N <= 1:
            return N
        else:
            return self.fib(N-1) + self.fib(N-2)

Solution().fib(6)
##

class Solution:
    def climbStairs(self, n):
        ans = 0
        if n==1:
            ans = 1
        elif n==2:
            ans = 2
        elif n>2:
            ans = self.climbStairs(n-1)+self.climbStairs(n-2)
        return ans
Solution().climbStairs(35)
##
class Solution:
    def climbStairs(self, n):
        dp = [1,2]
        for i in range(2, n):
            dp.append(dp[i-1]+dp[i-2])
        return dp[n-1]
Solution().climbStairs(35)

##
a = [-2,1,-3,4,-1,2,1,-5,4]
a = [-2,1]
a = [-2,-3,-1]

class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        lowSum = 0
        Sum = nums[0]
        maxSum = max(nums)
        for i in range(1, len(nums)):
            if Sum + nums[i] < nums[i]:
                lowSum = Sum + nums[i]
                Sum = nums[i]
            else:
                Sum += nums[i]
                maxSum = max(Sum, maxSum)
            print('low sum:{}  max sum:{}'.format(lowSum,Sum))
        return maxSum
Solution().maxSubArray(a)
##
s = "ahgcbg"
t = "ahbgdcahbgdc"

class Solution:
    def isSubsequence(self, s, t):
        print(s,t)
        if not s:
           return True
        if len(s) == 1:
            if s in t:
                return True

        istart = iend = 0

        for i,v in enumerate(t):
            if v==s[0]:
               istart = i
               break

        for i in range(len(t)-1, -1, -1):
            if t[i] ==s[-1]:
                iend = i
                break

        if istart < iend:
            if len(s)==2:
                return True

            print(s[1:-1], t[istart+1:iend])
            return self.isSubsequence(s[1:-1], t[istart+1:iend])
        return False

Solution().isSubsequence(s,t)

##

s = "ahgcbg"
t = "ahbgdcahbgdc"

class Solution:
    def isSubsequence(self, s, t):
        print(s,t)
        istart = iend = 0
        for i,v in enumerate(t):
               istart = i
               break
        print(s[1:-1], t[istart+1:iend])
        return self.isSubsequence(s[1:-1], t[istart+1:iend])

##
Solution().isSubsequence(s,t)
##
k=2
n=3

dp = []
dp.append((k,0))
dp.append((0,k**2))

print(dp)

for i in range(2, n):
    print(dp[i-1][1], k-1)
    first = (dp[i - 1][1] // k) * (k - 1)
    second = dp[i - 1][0] * k + dp[i - 1][1] * (k - 1)
    dp.append((first, second))
print(dp)
##

import numpy as np
import re
class NumArray:

    def __init__(self, nums):
        self.dp = np.zeros(len(nums), dtype = 'int64')
        if re.compile('[a-z]+').match(str(nums)):
            self.dp[0] = 0
        elif len(nums) == 1:
            try:
                self.dp[0] = sum(nums)
            except TypeError:
                pass
        else:
            self.dp = np.zeros(len(nums), dtype = 'int64')
            try:
                self.dp[0]=nums[0]
                self.dp[1]=self.dp[0]+nums[1]
            except IndexError:
                self.dp = np.zeros(len(nums), dtype = 'int64')

            for i in np.arange(2,len(nums)):
                self.dp[i] = self.dp[i-1]+nums[i]

    def sumRange(self, i, j):
        if self.dp.shape[0]>1:
            if i == 0 or j == 0:
                return self.dp[j]
            else:
                return self.dp[j]-self.dp[i-1]
        else:
            return self.dp[0]
##
nums = ['dd']
NumArray(nums).sumRange(0,2)
##

Input = [[17,2,17],[16,16,5],[14,3,19]]

class Solution:
        def minCost(self, costs):
##

Input = [2,7,9,3,1]
import numpy as np
class Solution:
        def rob(self, nums):
            if len(nums) == 0:
                return 0
            elif len(nums) == 1:
                return nums[0]

            ans = np.zeros(len(nums),dtype='int32')
            ans[0]=nums[0]
            ans[1]=nums[1]
            for i in np.arange(2,len(nums)):
                ans[i] = nums[i]+max(ans[:i-1])
            return max(ans)

Solution().rob(Input)
##

cost1 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
cost2 = [0, 0, 0, 1]
cost3 = [0, 0, 1, 1]
import numpy as np
class Solution:
        def minCostClimbingStairs(self, cost):
            if len(cost) == 0:
                return 0
            if len(cost) == 1:
                return cost[0]

            dp = np.zeros(len(cost),dtype='int32')
            dp[0]=cost[0]
            dp[1]=cost[1]
            for i in np.arange(2,len(cost)):
                dp[i] = min(cost[i]+dp[i-1], cost[i]+dp[i-2])
            print(dp)
            return min(dp[-1],dp[-2])

Solution().minCostClimbingStairs(cost1)
Solution().minCostClimbingStairs(cost2)
Solution().minCostClimbingStairs(cost3)
##



