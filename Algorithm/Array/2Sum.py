

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

A = [34,23,1,24,75,33,54,8]
K = 60

class Solution:
        def twoSumLessThanK(self, A, K):
            i=0
            j=len(A)-1
            maxSum = -1
            A_sorted = sorted(A)
            while i<j:
                sum = A_ass Solution:
        def twoSumLessThanK(self, A, K):
            i=0
            j=len(A)-1
            maxSum = -1
            A_sorted = sorted(A)
            while i<j:
                sum = A_sorted[i]+A_sorted[j]
                if sum < K:
                    maxSum = max(maxSum, A_sorted[i]+A_sorted[j])
                    i+=1
                else:
                    j-=1
            return maxSumorted[i]+A_sorted[j]
                if sum < K:
                    maxSum = max(maxSum, A_sorted[i]+A_sorted[j]
                    i+=1
                else:
                    j-=1
            return maxSum


##

numbers = [2,7,11,15]
target = 9

class Solution:
        def twoSum(self, numbers, target):
            i=0
            j=len(numbers)-1
            while i<j:
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]
                elif numbers[i]+numbers[j]>target:
                    j -= 1
                else:
                    i += 1
            return []

Solution().twoSum(numbers,target)


##
def twoSum1(nums, target):
    mydict = {}
    indexlist = []
    for (i,v) in enumerate(nums):
        compliment = target - v
        if compliment not in mydict:
            mydict[v] = i
        else:
            indexlist.extend([i,mydict[compliment]])
    return(indexlist)



nums=[1,2,3,4,6,7,5]
target=8
twoSum1(nums,target)

##
