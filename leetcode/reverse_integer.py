class Solution:
    def reverse(self, x):
        maxInt = 2**31 -1
        minInt = -1 * 2**31
        if x < 0:
            y = -1 * int (str(-x)[::-1])
        else:
            y = int(str(x)[::-1])
        
        if y > maxInt or y < minInt:
            return 0
        print(y)

    def reverse2(self, x):
        if x > 0:
            x = str(x)
            x = x[::-1]
            x = int(x)
        else:
            x = -x
            x = str(x)
            x = x[::-1]
            x = int(x)
            x = -x
        print(x)
        if x > -2147483648 and x < 2147483647:
            return x
        else:
            return 0


if __name__=="__main__":
    Solution().reverse2(2147483649990000000)
##

input = [4,2,3]
class Solution:

    def checkPossibility(self, nums):
        count = 0
        idx = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                idx = i
        print(count,idx)
        if count == 0:
            return True

        if count > 1:
            return False

        if count == 1:
            if idx == 0 or (
                idx - 1 >= 0 and idx + 2 <= len(nums) - 1
                and nums[idx] > nums[idx + 2]
                and nums[idx + 1] > nums[idx - 1]):
                return True
            else:
                return False

Solution().checkPossibility(input)

##
nums = [1,2,2,4]
d = {}
set(range(1, len(nums)+1))

class Solution:
    def findErrorNums(self, nums):
        for i in nums:
            if i not in d:
                d[i]=0
            else:
                d[i]+=1

##
Input=[17,13,11,2,3,5,7]
Input[-1:]
Input[-1]
Input[:-1]
Input.sort(reverse=True)
dp=[]
print(Input)
for num in Input:
    print('===')
    print(dp)
    print('---')
    dp = [num]+dp[-1:]+dp[:-1]
    print(num)
    print(dp[-1:])
    print(dp[:-1])
##


##
class Solution:
    def updateBoard(self, board, click):
        dirs = [[0,1], [0, -1], [1,0], [-1,0], [-1,-1], [-1,1], [1,-1], [1,1]]
        row = click[0]
        col = click[1]
        m = len(board)
        n = len(board[0])

        if (board[row][col] == 'M') or (board[row][col]=='X'):
            board[row][col]='X'
            return board
        num = 0
        for dir in dirs:
            newRow = dir[0]+row
            newCol = dir[1]+col

            if newRow>=0 and newCol>=0 and newRow<m and newCol<n and board[newRow][newCol]=='M':
                num+=1
        if num>0:
            board[row][col] = str(num)
            return board
        else:
            board[row][col] = 'B'
        for dir in dirs:
            newRow = dir[0]+row
            newCol = dir[1]+col
            if newRow>=0 and newCol>=0 and newRow<m and newCol<n and board[newRow][newCol]=='E':
                self.updateBoard(board, [newRow, newCol])

        return board

Input = [["E","E","E","E","E"],
         ["E","E","M","E","E"],
         ["E","E","E","E","E"],
         ["E","E","E","E","E"]]
click = [3,0]
Solution().updateBoard(Input,click)

##





         
