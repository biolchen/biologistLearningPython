words = ["gin", "zen", "gig", "msg"]

class Solution:
    def uniqueMorseRepresentations(self, words):
        import string
        from collections import Counter
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d = dict(zip(string.ascii_lowercase, morse_codes))
        morse_l = []
        for word in words:
            morse = ''
            for i in word:
                morse += d[i]
            morse_l.append(morse)
        return len(Counter(morse_l))
        
res = Solution().uniqueMorseRepresentations(words)
print(res)