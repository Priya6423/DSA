class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R,C=len(board),len(board[0])
        queue=deque()
        for r in range(R):
            for c in range(C):
                if (r in (0, R-1) or c in (0, C-1)) and board[r][c]=="O":
                    queue.append((r,c))
                    board[r][c]="#"
        directions=[(-1,0),(0,-1),(1,0),(0,1)]
        while queue:
            curr,curc=queue.popleft()
            for dr,dc in directions:
                newr,newc=curr+dr,curc+dc
                if 0<=newr<R and 0<=newc<C and board[newr][newc]=='O':
                    board[newr][newc]='#'
                    queue.append((newr,newc))
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O':       
                    board[r][c] = 'X'
                elif board[r][c] == '#':     
                    board[r][c] = 'O'
                       
                            
            


        