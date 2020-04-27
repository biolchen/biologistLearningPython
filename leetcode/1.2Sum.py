

'''
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

##
nums = [2, 7, 11, 15]
target = 9


class Solution:
    def twoSum(self, nums, target):
        l = len(nums)
        for i in range(l):
            for j in range(l):
                if j > i and nums[i] + nums[j] == target:
                    return [i, j]


##

class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, v in enumerate(nums):
            if target - v in d:
                return(d[target - v], i)
                break
            d[v] = i
        return ([])


Solution().twoSum(nums, target)

##
