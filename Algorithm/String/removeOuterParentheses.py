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