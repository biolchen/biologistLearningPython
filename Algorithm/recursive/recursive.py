##
'''
1137. N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.
'''
class Solution:
    def tribonacci(self, n):
        if n == 0:
            return 0
        if n<3:
            return 1
        else:
            return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)


Solution().tribonacci(27)
##


class Solution:
    def tribonacci(self, n):
        l = [0,1,1]

        if n < len(l):
            return l[n]
        else:
            for i in range(3,n+1):
                next_num = l[i-1]+ l[i-2]+ l[i-3]
                l.append(next_num)
        return l.pop()

Solution().tribonacci(25)

##
##
Solution().findContestMatch
