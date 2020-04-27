class Solution:
    def asteroidCollision(self, asteroids):
        res = []
        for i in asteroids:
            while res and i < 0 < res[-1]:
                if res[-1] < abs(i):
                    res.pop(-1)
                elif res[-1] == abs(i):
                    res.pop(-1)
                    break
                else:
                    break
            else:
                res.append(i)
        return res

asteroids = [-2, -1, 1, 2]
asteroids = [8, -8, 5, -10]
Solution().asteroidCollision(asteroids)





def Enquiry(lis1):
    if not lis1:
        return 1
    else:
        return 0

lis1 = []
if Enquiry(lis1):
    print ("The list is Empty")
else:
    print ("The list is not empty")