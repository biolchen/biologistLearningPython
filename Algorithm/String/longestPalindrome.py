class Solution:
    def longestPalindrome(self, s):
        maxLen = len(s)
        flag = False
        for i in set(s):
            count = s.count(i)
            if count%2==1:
                maxLen -= 1
                flag = True
        if flag:
            maxLen += 1
        return maxLen

res = Solution().longestPalindrome('abccccdd')
print(res)