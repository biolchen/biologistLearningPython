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

res = Solution().isPalindrome(a)
print(res)