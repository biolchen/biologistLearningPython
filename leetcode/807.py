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

Input=np.array([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]])

import numpy as np
class Solution:
    def numRookCaptures(self, board):
        Input = np.array(board)
        xy0 = np.argwhere(Input=='R')[0]
        res = 0
        for i in np.array([1,0]),np.array([0,1]),np.array([-1,0]),np.array([0,-1]):
            xy = xy0 + i
            while 0<= xy[0] <= 7 and 0<= xy[1] <= 7:
                if Input[xy[0],xy[1]] == 'p':
                    res += 1
                if Input[xy[0],xy[1]] != '.':
                    break
                xy = xy+i
        return res

Solution().numRookCaptures(Input)

##

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
a
a.
##

a = np.array([-1, 0, 1, 2, -1, -4])
from collections import Counter
import numpy as np
class Solution:
    def threeSum(self, nums):


Solution().threeSum(a)



##
words = ["dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin","ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb","ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl","boygirdlggnh","xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx","nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop","hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx","juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr","lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo","oxgaskztzroxuntiwlfyufddl","tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp","qnagrpfzlyrouolqquytwnwnsqnmuzphne","eeilfdaookieawrrbvtnqfzcricvhpiv","sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz","yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue","hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv","cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo","teyygdmmyadppuopvqdodaczob","qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs","qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs"]
chars = "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp"
chars='abcda'
l=list(chars)
l.remove('a')
l

class Solution:
        def countCharacters(self, words, chars):
            ans = 0
            for word in words:
                include = True
                char0 = list(chars)
                for letter in word:
                    if letter in char0:
                        char0.remove(letter)
                    else:
                        include = False
                if include:
                    ans+=len(word)
            return ans
Solution().countCharacters(words, chars)

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

Solution().plusOne(Input)

##
[i for i in str(11)]



class Solution:
        def countAndSay(self, n):
            x=10
            dp = ['']*x
            dp[0]='1'
            dp[1]='11'
            for i in range(2,n+1):
                count = 0
                l=len(dp[i-1])
                s=dp[i-1]
                #print(l,s)
                for j in range(l):
                    count+=1
                    print(j)
                    print(l,s)
                    if (j+1<l and s[j]!=s[j+1]):
                        dp[i]=dp[i]+str(count)+s[j]
                        count = 0
                dp[i]=dp[i]+str(count)+s[j]

            return dp
Solution().countAndSay(5)
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
a="A man, a plan, a canal: Panama"

class Solution:
    def isPalindrome(self, s):
        import string
        i=0
        j=len(s)-1
        while i<=j:
            if not s[i].isalnum():
                i+=1
                continue
            elif not s[j].isalnum():
                j-=1
                continue
            if s[i].lower() != s[j].lower():
                print(s[i],s[j])
                return False
            i+=1
            j-=1
        return True
##
Solution().isPalindrome(a)

##

from itertools import groupby
a = 'aaaba'
list(groupby(a))


##
data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
groups = []
uniquekeys = []
data = sorted(data, key=keyfunc)
for k, g in groupby(data, keyfunc):
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)
##




