##

s1 = "a" 
s2 = "ab"

from collections import Counter
class Solution:
        def checkInclusion(self, s1, s2):
            C = Counter(s1)    
            window = None
            k=len(s1)
            i=0
            while i<len(s2)-k+1:
                if i == 0:
                    window = Counter(s2[:len(s1)])
                    if C==window:
                        return True
                    print(window)
                    i+=1
                else:
                    minus = {s2[i-1]:1} 
                    plus = {s2[i+k-1]:1}
                    window -= minus
                    window += plus
                    print(window)
                    if C==window:
                        return True
                    i+=1
            return False
Solution().checkInclusion(s1,s2)
##


Input="ABC"
from itertools import permutations

class Solution:
        def numTilePossibilities(self, tiles):
            res = []
            for i in range(1, len(tiles)+1):
                res += list(permutations(tiles,i))
            return len(set(res))

Solution().numTilePossibilities(Input)
##

class Solution:
    def generate(self, numRows):
        n = 0 
        b = [1]
        res = []
        while n<numRows:
            res.append(b)
            b = [1] + [b[i]+b[i+1] for i in range(len(b)-1)] + [1]
            n+=1
        return res
Solution().generate(5)

##
S = "abbaca"
print(S)
##




