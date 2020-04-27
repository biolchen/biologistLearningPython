'''
544. Output Contest Matches
'''
##
class Solution:
    def findContestMatch(self, n):
        team = tuple(range(1, n + 1))
        while len(team) > 2:
            team = tuple(([team[i], team[~i]]) for i in range(len(team) // 2))
            print(team)


Solution().findContestMatch(8)
##
tuple(range(1, 9))[~0]
##
n = 8
while n > 1:
    print(range(n >> 1))
    n >>= 1
##


class Solution:
    def findContestMatch(self, n):
        team = tuple(range(1, n + 1))
        while len(team) > 2:
            team = tuple(([team[i], team[~i]]) for i in range(len(team) // 2))
            print(team)


Solution().findContestMatch(8)
##
