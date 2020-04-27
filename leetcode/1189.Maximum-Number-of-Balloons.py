##
text = "nlaebolko"

class Solution:
        def maxNumberOfBalloons(self, text):
            output = []
            a = "balloon"
            for c in 'balon':
                output.append(text.count(c)/'balloon'.count(c))
            return min(output)
##
