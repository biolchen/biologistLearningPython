
'''
Input: "(()())(())"
Output: "()()()"
Explanation: 
    The input string is "(()())(())", with primitive decomposition "(()())" +
    "(())".
    After removing outer parentheses of each part, this is "()()" + "()" =
    "()()()".
'''
##
Input= "(()())(())"
class Solution:
    def removeOuterParentheses(self,S):
        res= []
        count = 0
        i=0
        for j in range(len(S)):
            if S[j]=='(':
                count+=1
            elif S[j]==')':
                count-=1
            if count==0:
                res.append(S[i+1:j])
                i=j+1
        return "".join(res)
Solution().removeOuterParentheses(Input)
##
Input=[4,3,2,7,8,2,3,1]
class Solution:
        def findDisappearedNumbers(self, nums):
            ans = [] 
            a = set(range(1,len(nums)+1))
            b = set()
            for i in nums:
                b.add(i)
            return list(a-b)
SolutiofindDisappearedNumbers(Input)
##


Input= [1,2,3,4,5,6,7] 
k = 3

class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        while i<k:
            nums[:]=nums[-1:]+nums[:-1]
        return nums
Solution().rotate(Input,3)

##
