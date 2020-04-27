##
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
len(grid)

a =np.array([[1,2],[3,4],[5,6]])
for (x,y), value in np.ndenumerate(a):
    print(x,y)
##
import numpy as np
class Solution:
        def maxIncreaseKeepingSkyline(self, grid):
            grid = np.array(grid)
            newArr = np.zeros(grid.shape, dtype='int64')
            south_Max = np.max(grid, axis=0)
            west_Max = np.max(grid, axis=1)
            for (i,j),value in np.ndenumerate(grid):
                    newArr[i,j] = min(west_Max[i],south_Max[j])
            return np.sum(newArr-grid)

Solution().maxIncreaseKeepingSkyline(grid)
##


Input = [1,3,2,2,5,2,3,7]
for i in range(len(Input)-1,0,-1):
    print(Input[i])

##
from collections import Counter

class Solution:
        def findLHS(self, nums):
            ans = 0
            d = Counter(nums)
            for i in nums:
                if i+1 in d:
                    ans = max(ans, d[i]+d[i+1])
            return ans
Solution().findLHS(Input)
##
Input=[4,3,2,1]
class Solution:
        def plusOne(self, digits):
            digits[-1]+=1
            l=len(digits)
            for i in range(l-1, 0, -1):
                if digits[i]!=10:
                    break
                digit[i]=0
                digits[i-1] += 1
            if digits[0]==10:
                digits[0]=0
                digits.insert(0,1)

            return digits

res = Solution().plusOne(Input)
print(res)

##

