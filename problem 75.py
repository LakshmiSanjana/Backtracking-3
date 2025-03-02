# Word Search(https://leetcode.com/problems/word-search/)


# TC: O(m * n * 3^L) m^n for the board traversal and L is in the length of the word
# 3^L is for traversing all the other 3 directions
# SC: O(L) # length of the word recursive stack space

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.dirs = [[-1,0],[1,0],[0,-1],[0,1]]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.backtrack(board,i,j,0,word):
                        return True        
        return False
    
    def backtrack(self,board,r,c,idx,word):
        # base
        if idx == len(word):
            return True
        if r < 0 or c< 0 or r == len(board) or c == len(board[0]) or board[r][c] == '$':
            return False


        if board[r][c] == word[idx]:
        #logic
            board[r][c] = '$'
            for d in self.dirs:
                nr = d[0] + r
                nc = d[1] + c
                if self.backtrack(board,nr,nc,idx+1,word):
                    return True
        # backtrack
            board[r][c] = word[idx]

        return False

########### BFS #######################

# TC is same as above
# SC: O(m * n) --> for the queue space


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        
        self.dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.bfs(board,i,j,self.dirs,word):
                        return True
        
        return False
    
    def bfs(self,board,r,c,dirs,word):
        q = deque()
        q.append((r,c,0,{(r,c)}))
        while q:
            i,j,idx,visited = q.popleft()

            if idx == len(word) - 1:
                return True

            for d in self.dirs:
                nr = i + d[0]
                nc = j + d[1]

                if nr>=0 and nr < len(board) and nc >= 0 and nc < len(board[0]) and (nr,nc) not in visited:
                    if board[nr][nc] == word[idx+1]:
                        new_visited = visited.copy()
                        new_visited.add((nr,nc))
                        q.append((nr,nc,idx+1,new_visited))
        
        return False