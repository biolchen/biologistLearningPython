Input=np.array([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]])

import numpy as np
class Solution:
    def numRookCaptures(self, board):
        Input = np.array(board)
        xy0 = np.argwhere(Input=='R')[0]
        res = 0
        for i in np.array([1,0]),np.array([0,1]),np.array([-1,0]),np.array([0,-1]):
            xy = xy0 + i
            while 0<= xy[0] <= 7 and 0<= xy[1] <= 7:
                if Input[xy[0],xy[1]] == 'p':
                    res += 1
                if Input[xy[0],xy[1]] != '.':
                    break
                xy = xy+i
        return res

Solution().numRookCaptures(Input)