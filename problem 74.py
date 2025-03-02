# N Queens(https://leetcode.com/problems/n-queens/)


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.board = [[False] * n for _ in range(n)]
        self.result = []
        self.helper(self.board,0,self.result)
        return self.result
    
    def helper(self,board,r,result):
        # base

        if ( r == len(self.board)):
            li = []
            for i in range (len(self.board)):
                sb = []
                for j in range (len(self.board[0])):
                    if (self.board[i][j]):
                        sb.append("Q")
                    else:
                        sb.append(".")
                li.append("".join(sb))
            self.result.append(li)
            return

        #logic
        for c in range(len(self.board[0])):
            if(self.issafe(self.board,r,c)):
                # action
                self.board[r][c] = True
                # recurse
                self.helper(self.board,r+1,self.result)
                #backtrack
                self.board[r][c] = False
    
    def issafe(self,board,r,c):

        # column up
        for i in range(r):
            if(self.board[i][c]):
                return False
        
        # up left
        i = r
        j = c
        while i>=0 and j>=0:
            if(self.board[i][j]):
                return False
            i-=1
            j-=1
        
        #up right
        i = r
        j = c

        while i>=0 and j< len(self.board[0]):
            if(self.board[i][j]):
                return False
            i-=1
            j+=1

        return True

# TC: O(n!) -->
#In the first row, we have N choices for placing a queen.
#In the second row, we have at most N-1 choices due to conflicts.
#In the third row, we have at most N-2 choices, and so on.
#This results in a branching factor of approximately N * (N-1) * (N-2) * ... * 1 = N!.

# SC: O( n^2 * n!) --> board space n^2 and recursive stack n!