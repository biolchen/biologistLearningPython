##
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        import numpy as np
        indices = dict(zip(keyboard, np.arange(len(keyboard))))
        sum = 0
        pre_index = 0
        post_index = 0
        for i in word:
            post_index = indices[i]
            sum += np.absolute(post_index-pre_index)
            pre_index = post_index
        return sum
##
a = 'pqrstuvwxyzabcdefghijklmno'

Solution().calculateTime(a, 'leetcode')
        

##

