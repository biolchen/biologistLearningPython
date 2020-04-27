
ass Solution:
    def hammingDistance(self, x: int, y: int) -> int:


        '{0:04b}'.format(x)
        '{0:04b}'.format(y)





'{0:00b}'.format(40)

bin(1)
bin(40)
20^40
40+2


get_bin = lambda x, n: format(x,'b').zfill(n)
get_bin(1,100)



class Solution:
    def removeVowels(self, S: str) -> str:
        ''.join([i for i in S if i not in 'aeiou'])


##

class Solution:
    def isArmstrong(self, N: int) -> bool:
        l=[int(d) for d in str(n)]
        return N == np.sum(list(map(lambda x:x**len(l), l)))



##
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        num = []
        first = 0
        last = len(item_list)-1
        found = False
        while( first<=last and not found):
            mid = (first + last)//2
            if item_list[mid] == item :
                found = True
            else:
                if item < item_list[mid]:
                    last = mid - 1
                else:
                    first = mid + 1	
        return found
	
print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5))



##
class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        ans = []
        for i,v in enumerate(A):
            if i == A[i]:
                ans.append(A[i])
        
        if len(ans) == 0:
            return -1
        else:
            return ans[0]
            

##
A = "abcd"
B = "cdabcdab"
B in A*3
B.split(A)
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if len(A) >= len(B):
            if B in A:
                return 1 
            if B in A*2:
                return 2
            else:
                return -1
        else:

        n = 1
        len0 = len(A)
        if len(A) < len(B) and (B not in A*n):
            n += 1
            A = A*n
            print(A*n)
        return int(len(A)/len0)

Solution().repeatedStringMatch(A, B)


##
'''
Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.
'''
##
Input = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

##

class Solution:
    def highFive(self, items):
        from collections import defaultdict 
        from heapq import nlargest
        import numpy as np
        d = defaultdict(list) 
        output = []
        for i in items:
            d[i[0]].append(i[1])

        for k,v in d.items():
            print(k,v)
            output2 = []
            output2.append(k)
            result = np.sum(nlargest(5,v))//5
            output2.append(result)
            output.append(output2)

        return output
        
##


words = ["gin", "zen", "gig", "msg"]

class Solution:
    def uniqueMorseRepresentations(self, words):
        import string
        from collections import Counter
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d = dict(zip(string.ascii_lowercase, morse_codes))
        morse_l = []
        for word in words:
            morse = ''
            for i in word:
                morse += d[i]
            morse_l.append(morse)
        return len(Counter(morse_l))
Solution().uniqueMorseRepresentations(words)
##
            

[0,0,1,1][::-1]


Input = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

##

class Solution:
    def flipAndInvertImage(self, A):
        a = map(lambda x: x[::-1], A)
        output = [list(map(lambda x: 1 if x==0 else 0, i)) for i in list(a)]
        return output

Solution().flipAndInvertImage(Input)
##


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd_l = []
        even_l = []
        for i in A:
            if i%2 == 0:
                even_l.append(i)
            else:
                odd_l.append(i)
        return even_l+odd_l
            

##
class Solution:
    def sumOfDigits(self, A):
        from heapq import nsmallest
        import numpy as np
        res = np.sum([int(i) for i in str(nsmallest(1,A)[0])])
        if res%2 == 0:
            return 1
        else: 
            return 0

Solution().sumOfDigits([99,77,33,66,55])

##

left = 1
right = 22

print(output)

##

class Solution:
    def selfDividingNumbers(self, left, right):
        import numpy as np
        output = []
        for i in np.arange(left, right+1):
            if i%10 == 0:
                continue
            elif ('0' not in [j for j in str(i)]) and np.sum([i%int(j) for j in str(i)]) == 0:
                output.append(i)
        return output
         
Solution().selfDividingNumbers(66,708) 
##


sorted(list(map(lambda x: x**2, [-4,-1,0,3,10])))

a= [0,2,1,0]

np.argmax(a)
##
S = "IDIDDDDD"

class Solution:
    def diStringMatch(self, S):
        import numpy as np
        low = 0
        high = len(S)
        output = []

        for i in np.arange(len(S)):
            if S[i] =='I':
                output.append(low)
                low += 1
            else:
                output.append(high)
                high -= 1
        return output + [low]
Solution().diStringMatch(S)
##

class RecentCounter:

    def __init__(self):
        

    def ping(self, t: int) -> int:
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

##
Input = ["cba","daf","ghi"]
Input = ["rrjk","furt","guzm"]
Input = ["cba","daf","ghi"]
class Solution:
    def minDeletionSize(self, A):
        from functools import reduce
        import numpy as np
        import string
        d = dict(zip(string.ascii_lowercase, list(np.arange(len(string.ascii_lowercase)))))
        def c(S):
            return [d[x] for x in S]
        e = np.array(list(map(c, A))).T
        print(e)
        if e.shape[0] == 1:
            return 0
        result = list(map(lambda x: np.array_equal(sorted(x),x), e))
        print(result)
        return len(result)-np.count_nonzero(result)

Solution().minDeletionSize(Input)
##
Input = [11,10,11,1,1,1,1,12,13]

class Solution:
    def largestUniqueNumber(self, A):
        d = {}
        for num in A:
            if num in d.keys():
                d[num] +=1
            else:
                d[num]=1
        max_num = -1
        for k,v in d.items():
            if v==1:
                max_num = max(max_num, k)
        return max_num
Solution().largestUniqueNumber(Input)
##

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        import numpy as np
        d1 = dict(zip(list(np.arange(len(heights))),heights))
        d2 = dict(zip(list(np.arange(len(heights))),sorted(heights)))

        count = 0
        for i in zip(d1.values(),d2.values()):
                if i[0]!=i[1]:
                    count += 1
        return count 


'''
Given an array A of integers, return the number of non-empty continuous subarrays that satisfy the following condition:

The leftmost element of the subarray is not larger than other elements in the subarray.

Example 1:
Input: [1,4,2,5,3]
Output: 11
Explanation: There are 11 valid subarrays: [1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3].

Example 2:
Input: [3,2,1]
Output: 3
Explanation: The 3 valid subarrays are: [3],[2],[1].

Example 3:
Input: [2,2,2]
Output: 6
Explanation: There are 6 valid subarrays: [2],[2],[2],[2,2],[2,2],[2,2,2].
'''
##
nums = [1,4,2,5,3]
def p(nums, n):
    output = []
    while len(nums) > 2:
        nums.pop(n)
        if sorted(nums)[0]==nums[0]:
            print(nums)
    return output
##
test_str = [42,16,57,53,70,36,74,14,70,59,57,32,0,74,44,18,34,15,59,72,77,24,50,68,35,10,40,63,11,35,29,26,20,75,26,7,6,76,1,66,67,80,15,55,53,24,73,78,8,78,22,18,61,48,52,24,57,63,12,32,30,31,73,48,21,5,7,9,6,4,52,39,6,50,22,61,30,4,78,52,33,76,79,23,11,45,81,59,72,10,70,40,52,22,63,0,39,71,34,71,70,55,72,2,67,39,15,69,39,4,16,54,70,31,72,61,7,76,18,55,22,9,17,49,63,54,8,55,55,9,77,71,18,27,1,47,62,52,8,46,15,76,44,44,32,69,46,58,47,34,8,14,39,42,56,19,6,36,60,37,79,55,70,60,10,54,35,72,76,3,13,73,6,20,56,22,76,67,11,75,27,9,38,73,72,21,79,57,37,59,45,72,59,57,5,81,33,1,20,77,21,15,9,57,20,80,22,21,26,14,76,7,59,65,37,49,62,4,36,7,50,11,73,39,39,27,77,22,68,3,7,46,60,53,11,39,46,54,21,2,26,10,46,20,64,23,76,0,67,80,54,39,21,10,69,75,59,39,47,57,37,70,17,79,15,18,58,23,37,33,12,11,35,17,5,73,36,21,21,62,79,25,25,41,80,77,50,0,23,62,75,3,66,34,41,69,80,79,14,8,1,21,25,42,56,26,63,79,60,25,65,78,9,65,74,39,49,37,4,3,58,14,56,49,64,58,79,80,27,47,73,66,70,4,30,50,45,44,13,16,16,21,74,71,10,77,16,79,81,6,0,80,28,14,30,55,66,53,13,13,18,65,29,69,57,9,40,67,14,67,45,56,72,41,24,13,18,60,17,40,48,10,27,23,55,8,51,75,4,47,66,34,33,11,61,80,79,29,39,52,66,38,71,41,62,1,64,19,71,74,55,52,53,50,75,41,76,46,22,60,42,35,70,17,25,33,34,64,50,8,12,56,75,15,41,56,18,78,7,71,10,36,81,44,11,57,44,5,68,68,50,27,11,59,4,66,38,78,10,63,77,55,0,23,6,12,29,8,30,80,47,11,20,18,54,79,58,39,46,76,29,0,73,48,34,1,57,13,9,43,50,57,52,13,77,49,68,72,39,57,51,76,35,44,31,4,8,75,26,68,14,69]

class Solution:
    def validSubarrays(self, nums):
        import numpy as np
        res = [nums[i: j] for i in np.arange(len(nums)) for j in np.arange(i + 1, len(nums) + 1) if (nums[i: j][0] == sorted(nums[i: j])[0])]
        return len(res)

Solution().validSubarrays(test_str)



##
'''
Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.

Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]
Example 2:

Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]
'''


##
text = "alice is a good girl she is a good student"
first = "a"
second = "good"
##
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        import numpy as np
        output = []
        sentence = text.split(' ')
        for i in np.arange(1,len(sentence)-1):
            if sentence[i-1] == first and sentence[i] == second:
                output.append(sentence[i+1])
        return output




