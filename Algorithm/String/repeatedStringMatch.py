A = "abcd"
B = "cdabcdab"
B in A*3
B.split(A)
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if len(A) >= len(B):
            if B in A:
                return 1 
            if B in A*2:
                return 2
            else:
                return -1
        else:
            n = 1
            len0 = len(A)
            if len(A) < len(B) and (B not in A*n):
                n += 1
                A = A*n
                print(A*n)
        return int(len(A)/len0)

res = Solution().repeatedStringMatch(A, B)
print(res)