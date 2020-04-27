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