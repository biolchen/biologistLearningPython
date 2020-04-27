text = "nlaebolko"

# LeetCode 1189. Maximum Number of Balloons
class Solution:
        def maxNumberOfBalloons(self, text):
            output = []
            a = "balloon"
            for c in 'balon':
                output.append(text.count(c)/'balloon'.count(c))
            return min(output)
##

res=Solution().maxNumberOfBalloons(text)
print(res)
# 1.0